import statistics
from abc import ABC, abstractmethod
from collections import deque

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

openers = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def solve_part_one(lines):
    # A corrupted line is one, that closes with the wrong character.
    # A corrupted chunk is a corrupted line within a line.
    # A line is also considered corrupted when it contains a corrupted chunk.
    instruction_lines = [list(map(make_instruction, line)) for line in lines]
    score = 0
    for instruction_line in instruction_lines:
        is_corrupted, last_symbol, _ = is_corrupted_line(instruction_line)
        if is_corrupted:
            score += points[closers[last_symbol]]
    return score


def solve_part_two(lines):
    instruction_lines = [list(map(make_instruction, line)) for line in lines]
    incomplete_lines = [line for line in instruction_lines if not is_corrupted_line(line)[0]]
    memories = [is_corrupted_line(line)[2] for line in incomplete_lines]
    completion_strings = [calculate_completion_string(memory) for memory in memories]
    completion_string_scores = [calculate_completion_string_score(completion_string) for completion_string in completion_strings]
    sorted_completion_string_scores = sorted(completion_string_scores)
    return statistics.median(sorted_completion_string_scores)


def is_corrupted_line(line):
    memory = deque()
    last_symbol = None
    for instruction in line:
        is_correct_character, memory = instruction.execute(memory=memory)
        last_symbol = instruction.symbol
        if not is_correct_character:
            return True, last_symbol, memory
    return False, last_symbol, memory


def calculate_completion_string(memory):
    ret = []
    while len(memory) != 0:
        ret += [closers[memory.pop()]]
    return ''.join(ret)


def calculate_completion_string_score(completion_string):
    score = 0
    for character in completion_string:
        score *= 5
        score += autocomplete_points[character]
    return score


class Instruction(ABC):

    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def execute(self, memory, *kwargs):
        pass


class PushInstruction(Instruction):

    def __init__(self, symbol):
        super().__init__(symbol)

    def execute(self, memory, *kwargs):
        cpy = memory.copy()
        cpy.append(self.symbol)
        return True, cpy


class PopInstruction(Instruction):

    def __init__(self, symbol):
        super().__init__(openers[symbol])

    def execute(self, memory, *kwargs):
        cpy = memory.copy()
        symbol = cpy.pop()
        return symbol == self.symbol, cpy


def make_instruction(character):
    if character in openers.values():
        return PushInstruction(character)
    elif character in closers.values():
        return PopInstruction(character)
    else:
        raise ValueError(f"There is no instruction corresponding to character: '{character}'")



