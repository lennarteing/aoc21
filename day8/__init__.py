import re
import numpy as np

import defaults


def solve_part_one(lines):
    codes, outputs, inputs = format_input(lines)
    lengths = np.array([len(string) for line in outputs for string in line])
    number_of_ones = len(lengths[lengths == 2])
    number_of_fours = len(lengths[lengths == 4])
    number_of_sevens = len(lengths[lengths == 3])
    number_of_eights = len(lengths[lengths == 7])
    return number_of_eights + number_of_sevens + number_of_fours + number_of_ones


def solve_part_two(lines):
    codes, outputs, inputs = format_input(lines)
    for idx, val in enumerate(inputs):
        solve_line(val, outputs[idx])


def solve_line(inputs, outputs):
    possibilities = {
        'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    }
    for item in inputs:
        s = set([char for char in item])
        if len(s) == 2:
            possibilities['c'] = s
            possibilities['f'] = s
        elif len(s) == 4:
            possibilities['b'] = s
            possibilities['c'] = s
            possibilities['d'] = s
            possibilities['f'] = s
        elif len(s) == 3:
            possibilities['a'] = s
            possibilities['c'] = s
            possibilities['f'] = s
    possibilities['a'] = set.union(possibilities['c'], possibilities['f']) - possibilities['a']


def format_input(lines):
    codes = [re.split('\| |\ ', line) for line in lines]
    codes = np.array([[line[:10], line[-4:]] for line in codes], dtype=object)
    rot_codes_view = np.rot90(codes)
    outputs = rot_codes_view[0]
    inputs = rot_codes_view[1]
    return codes, outputs, inputs


if __name__ == '__main__':
    content = defaults.puzzle_input_now(2021, 8)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
