def solve_part_one(lines):
    # Every laternfish can be represented as the number of days it will
    # take for it to produce a new laternfish
    # After their first cycle lanternfish will take 9 instead od 7 days / +2 days
    # The timer includes 0 as a valid value.
    # 3->2->1->0->Creation->6
    # Creation means adding a new lanternfish to the list with 8. mod 7?

    lanternfish = [int(fish) for fish in [line.split(',') for line in lines][0]]
    lanternfish_dict = {}
    for spawn_timer in range(9):
        lanternfish_dict[spawn_timer] = lanternfish.count(spawn_timer)
    for _ in range(80):
        lanternfish_dict = step_part_one(lanternfish_dict)
    return sum(lanternfish_dict.values())


def solve_part_two(lines):
    # Same but longer
    lanternfish = [int(fish) for fish in [line.split(',') for line in lines][0]]
    lanternfish_dict = {}
    for spawn_timer in range(9):
        lanternfish_dict[spawn_timer] = lanternfish.count(spawn_timer)
    for _ in range(256):
        lanternfish_dict = step_part_one(lanternfish_dict)
    return sum(lanternfish_dict.values())


def step_part_one(lanternfish_dict):
    number_of_new_spawns = lanternfish_dict[0]
    for spawn_timer in range(7):
        lanternfish_dict[spawn_timer - 1] = lanternfish_dict[spawn_timer]
    lanternfish_dict[6] = lanternfish_dict[-1]
    lanternfish_dict[6] += lanternfish_dict[7]
    lanternfish_dict[7] = lanternfish_dict[8]
    lanternfish_dict[8] = lanternfish_dict[-1]
    del lanternfish_dict[-1]
    return lanternfish_dict
