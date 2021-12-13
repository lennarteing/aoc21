import statistics
from abc import ABC, abstractmethod
from collections import deque

import defaults

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
    completion_string_scores = [calculate_completion_string_score(completion_string) for completion_string in
                                completion_strings]
    sorted_completion_string_scores = sorted(completion_string_scores)
    return statistics.median(sorted_completion_string_scores)


def is_corrupted_line(line):
    memory = deque()
    last_symbol = None
    for instruction in line:
        is_correct_character, memory = instruction.execute(memory)
        last_symbol = instruction.instruction_parameters['symbol']
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


class PushInstruction(defaults.Instruction):

    def execute(self, system_state):
        cpy = system_state.copy()
        cpy.append(self.instruction_parameters['symbol'])
        return True, cpy


class PopInstruction(defaults.Instruction):

    def __init__(self, instruction_parameters):
        super().__init__({'symbol': openers[instruction_parameters['symbol']]})

    def execute(self, system_state):
        cpy = system_state.copy()
        symbol = cpy.pop()
        return symbol == self.instruction_parameters['symbol'], cpy


def make_instruction(character):
    if character in openers.values():
        return PushInstruction({'symbol': character})
    elif character in closers.values():
        return PopInstruction({'symbol': character})
    else:
        raise ValueError(f"There is no instruction corresponding to character: '{character}'")


if __name__ == '__main__':
    content = defaults.puzzle_input_now(2021, 10)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
