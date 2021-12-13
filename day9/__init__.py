import matplotlib
import skimage
import operator

import numpy as np

from scipy.ndimage import generic_filter
from functools import reduce

import defaults

adjacency_footprint = np.array([[False, True, False],
                                [True, True, True],
                                [False, True, False]])


def solve_part_one(lines):
    numbers = format_input(lines)
    padded_numbers = np.pad(numbers, 1, constant_values=10)
    risk_levels = padded_numbers[lowpoint_locations(padded_numbers)] + 1
    return int(sum(risk_levels))


def solve_part_two(lines):
    numbers = format_input(lines)
    padded_numbers = np.pad(numbers, 1, constant_values=10)
    x, y = lowpoint_locations(padded_numbers)
    locations = list(map(tuple, np.rot90(np.array([x, y]))))
    basins = {location: set(basin(location, [], padded_numbers)) for location in locations}
    sorted_basins = sorted(basins.values(), key=len, reverse=True)
    three_biggest_basins = sorted_basins[:3]
    return reduce(operator.mul, map(len, three_biggest_basins), 1)


def lowpoint_locations(image):
    marked_lowpoints = generic_filter(image, lowpoint_kernel, footprint=adjacency_footprint)
    return np.where(marked_lowpoints == 0)


# depth first search
def basin(location, current_basin, padded_numbers):
    ret = [location]
    if padded_numbers[location] < padded_numbers[(location[0], location[1] - 1)] < 9 and (location[0], location[1] - 1) not in current_basin:
        ret += basin((location[0], location[1] - 1), current_basin, padded_numbers)
    if padded_numbers[location] < padded_numbers[(location[0], location[1] + 1)] < 9 and (location[0], location[1] + 1) not in current_basin:
        ret += basin((location[0], location[1] + 1), current_basin, padded_numbers)
    if padded_numbers[location] < padded_numbers[(location[0] - 1, location[1])] < 9 and (location[0] - 1, location[1]) not in current_basin:
        ret += basin((location[0] - 1, location[1]), current_basin, padded_numbers)
    if padded_numbers[location] < padded_numbers[(location[0] + 1, location[1])] < 9 and (location[0] + 1, location[1]) not in current_basin:
        ret += basin((location[0] + 1, location[1]), current_basin, padded_numbers)
    return ret + current_basin


def lowpoint_kernel(a):
    return 0 if a[2] < a[0] and a[2] < a[1] and a[2] < a[3] and a[2] < a[4] else 10


def format_input(lines):
    return np.array([list(map(lambda x: int(x), list(line))) for line in lines], dtype=np.float)


def draw_image(image):
    skimage.io.imshow(image)
    matplotlib.pyplot.show()


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 9)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))

