import collections

import defaults
import re


def solve_part_one(lines):
    polymer, rules = format_input(lines)
    for _ in range(10):
        polymer = apply_rules_once(polymer, rules)
    most_common_char = most_common(polymer)
    least_common_char = least_common(polymer)
    return most_common_char[1] - least_common_char[1]


def solve_part_two(lines):
    polymer, rules = format_input(lines)
    insertions = into_insertions(rules)
    polymer_windows = [window for window in defaults.sliding_window(polymer, n=2)]
    string_polymer_windows = [''.join(window) for window in polymer_windows]
    window_counts = {}
    char_counts = {}
    for window in string_polymer_windows:
        if window not in window_counts:
            window_counts[window] = 1
        else:
            window_counts[window] += 1
    for char in polymer:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for _ in range(40):
        tmp_window_counts = window_counts.copy()
        for window, count in tmp_window_counts.items():
            for insertion in insertions[window]:
                if insertion not in window_counts:
                    window_counts[insertion] = count
                else:
                    window_counts[insertion] += count
            window_counts[window] -= count
            if window_counts[window] == 0:
                del window_counts[window]
            if insertion[0] in char_counts:
                char_counts[insertion[0]] += count
            else:
                char_counts[insertion[0]] = count
    max_c = max(char_counts, key=char_counts.get)
    min_c = min(char_counts, key=char_counts.get)
    return char_counts[max_c] - char_counts[min_c]


def apply_rules_once(polymer, rules):
    ret = "" + polymer[0]
    for window in defaults.sliding_window(polymer, n=2):
        append_value = ''
        if ''.join(window) in rules:
            append_value += rules[''.join(window)]
        append_value += window[1]
        ret += append_value
    return ret


def into_insertions(rules):
    ret = {}
    for key, val in rules.items():
        insertions = [key[0] + val, val + key[1]]
        ret[key] = insertions
    return ret


def most_common(polymer):
    return collections.Counter(polymer).most_common(1)[0]


def least_common(polymer):
    return collections.Counter(polymer).most_common()[-1]


def format_input(lines):
    polymer_template, rules = None, None
    split_idx = lines.index('')
    polymer_template_line, rule_lines = [lines[: split_idx], lines[split_idx + 1:]]
    polymer_template = polymer_template_line[0]
    rule_pattern = r"(?P<in>\w+) -> (?P<out>\w)"
    rules = {match.group('in'): match.group('out') for match in [re.match(rule_pattern, rule) for rule in rule_lines]}
    return polymer_template, rules


if __name__ == '__main__':
    content = defaults.puzzle_input_now(2021, 14)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
