import defaults
from day2 import solve_part_two, solve_part_one

if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 2)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
