from collections import deque

import defaults


def solve_part_one(content):
    return sum(map(lambda win: 1 if win[1] > win[0] else 0, defaults.sliding_window(content, n=2)))


def solve_part_two(content):
    ret = map(sum, defaults.sliding_window(content, n=3))
    return solve_part_one(list(ret))


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 1)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))

