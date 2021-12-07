from day4 import solve_part_one, solve_part_two

if __name__ == '__main__':

    # Read file from input and transform into array of integers.
    filename = "../resources/day4input"
    with open(filename) as f:
        content = f.readlines()
    content = [line.strip() for line in content]

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))