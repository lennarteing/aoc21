import numpy as np

from enum import Enum
from abc import ABC, abstractmethod

import defaults


def solve_part_one(content):
    instruction_set = list(map(convert_line, content))
    movement_vectors = list(map(lambda normalization: normalization[0] * normalization[1], instruction_set))
    endposition = sum(movement_vectors)
    return endposition[0] * endposition[1]


def solve_part_two(content):
    instruction_set = list(map(convert_to_instruction, content))
    memory = (0, 0, 0)
    for instruction in instruction_set:
        memory = instruction.execute(memory)
    return memory[0] * memory[1]


def convert_line(line):
    instruction, value = line.split()
    if instruction == 'forward':
        instruction = InstructionCode.FORWARD
    elif instruction == 'down':
        instruction = InstructionCode.DOWN
    elif instruction == 'up':
        instruction = InstructionCode.UP
    return np.array(instruction.value), int(value)


def convert_to_instruction(line):
    instruction, value = line.split()
    if instruction == 'forward':
        instruction = ForwardInstruction({'value': int(value)})
    elif instruction == 'down':
        instruction = DownInstruction({'value': int(value)})
    elif instruction == 'up':
        instruction = UpInstruction({'value': int(value)})
    return instruction


class InstructionCode(Enum):
    FORWARD = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


class ForwardInstruction(defaults.Instruction, ABC):

    def execute(self, system_state):
        hor, vert, aim = system_state
        hor += self.instruction_parameters['value']
        vert += self.instruction_parameters['value'] * aim
        return hor, vert, aim


class DownInstruction(defaults.Instruction, ABC):

    def execute(self, system_state):
        hor, vert, aim = system_state
        aim += self.instruction_parameters['value']
        return hor, vert, aim


class UpInstruction(defaults.Instruction, ABC):

    def execute(self, system_state):
        hor, vert, aim = system_state
        aim -= self.instruction_parameters['value']
        return hor, vert, aim


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 2)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
