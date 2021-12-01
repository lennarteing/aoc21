def solve_part_one(content):
    return sum(map(lambda entry: 0 if entry[0] == 0 else 1 if content[entry[0]] > content[entry[0] - 1] else 0, enumerate(content)))


def solve_part_two(content):
    return "y"
