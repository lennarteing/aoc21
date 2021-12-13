import numpy as np

from scipy.ndimage import generic_filter

import defaults


def solve_part_one(lines):
    octopi = format_input(lines)
    total_flashes = 0
    for _ in range(100):
        octopi = iteration(octopi)
        total_flashes += len(octopi[octopi == 0])
    return total_flashes


def solve_part_two(lines):
    octopi = format_input(lines)
    count = 0
    while True:
        octopi = iteration(octopi)
        count += 1
        if np.array_equal(octopi, np.zeros(shape=(10, 10))):
            break
    return count


def format_input(lines):
    return np.array([int(c) for line in lines for c in line]).reshape((10, 10))


def iteration_kernel(window):
    if window[4] == -1:
        return -1
    if window[4] > 9:
        return -1
    neighbors = np.append(window[:4], window[5:])
    indices_if_higher_numbers = neighbors > 9
    higher_neighbors = neighbors[indices_if_higher_numbers]
    return window[4] + len(higher_neighbors)


def iteration(octopi):
    old_octopi = np.copy(octopi)
    octopi = np.add(octopi, 1)
    while not np.array_equal(octopi, old_octopi):
        old_octopi = np.copy(octopi)
        octopi = apply_padding(octopi)
        octopi = generic_filter(octopi, iteration_kernel, size=(3, 3))
        octopi = remove_padding(octopi)
    octopi[octopi == -1] = 0
    return octopi


def apply_padding(octopi):
    return np.pad(octopi, pad_width=1, mode='constant', constant_values=-1)


def remove_padding(octopi):
    return octopi[1: -1, 1: -1]


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 11)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
