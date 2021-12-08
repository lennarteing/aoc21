import re
import numpy as np


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
    #Started golfing here. Look into golfed.
    pass


def format_input(lines):
    codes = [re.split('\| |\ ', line) for line in lines]
    codes = np.array([[line[:10], line[-4:]] for line in codes], dtype=object)
    rot_codes_view = np.rot90(codes)
    outputs = rot_codes_view[0]
    inputs = rot_codes_view[1]
    return codes, outputs, inputs
