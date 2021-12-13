from defaults import puzzle_input_now
from day11 import solve_part_one, solve_part_two

if __name__ == '__main__':

    content = puzzle_input_now(2021, 11)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))