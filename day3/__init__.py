import defaults


def solve_part_one(content):
    numbers = map(str_to_bin_int, content)
    gamma = most_common_bit_number(numbers)
    epsilon = least_common_bit_number(numbers)
    return gamma * epsilon


def solve_part_two(content):
    pass


def most_common_bit_number(numbers):
    backup = list(numbers)
    most_common_bits = [most_common_bit_at(backup, idx) for idx in range(12)]
    return str_to_bin_int(''.join([str(bit) for bit in most_common_bits]))


def least_common_bit_number(numbers):
    return bit_not(most_common_bit_number(numbers))


def most_common_bit_at(numbers, pos):
    backup = list(numbers)
    bits_at_pos = list(map(lambda num: bit_at(num, pos), backup))
    return 1 if sum(bits_at_pos) >= len(list(backup)) / 2 else 0


def least_common_bit_at(numbers, pos):
    return bit_not(most_common_bit_at(numbers, pos))


def bit_not(n, num_bits=12):
    return (1 << num_bits) - 1 - n


def bit_at(num, pos):
    return (num >> pos) % 2


def str_to_bin_int(string):
    return int(string, 2)


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 3)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
