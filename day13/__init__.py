import re

import numpy as np

import defaults


def solve_part_one(lines):
    points, fold_instructions = format_input(lines)
    points = fold_instructions[0].execute({'points': points})
    return len(points)


def solve_part_two(lines):
    points, fold_instructions = format_input(lines)
    for instruction in fold_instructions:
        points = instruction.execute({'points': points})
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    paper = np.zeros(shape=(max_x + 1, max_y + 1))
    for point in points:
        paper[point] = 1
    return "\n" + str(paper)


def format_input(lines):
    split_idx = lines.index('')
    point_lines, instruction_lines = [lines[: split_idx], lines[split_idx + 1:]]
    point_pattern = r"(?P<x>\d+),(?P<y>\d+)"
    points = set([(int(match.group('x')), int(match.group('y'))) for match in [re.match(point_pattern, point_line) for
                                                                               point_line in point_lines]])
    instruction_pattern = r"fold along (?P<direction>[xy])=(?P<value>\d+)"
    instruction_line_matches = [re.match(instruction_pattern, instruction_line) for
                                instruction_line in instruction_lines]
    instructions = [HorizontalFoldInstruction({'value': int(match.group('value'))}) if match.group('direction') == 'y'
                    else VerticalFoldInstruction({'value': int(match.group('value'))}) for
                    match in instruction_line_matches]
    return points, instructions


class HorizontalFoldInstruction(defaults.Instruction):

    def execute(self, system_state, additional_parameters=dict()):
        points_below = {point for point in system_state['points'] if point[1] > self.instruction_parameters['value']}
        points_above = {point for point in system_state['points'] if point not in points_below}
        mirrored_points_below = {(point[0], 2 * self.instruction_parameters['value'] - point[1]) for point in
                                 points_below}
        return set.union(points_above, mirrored_points_below)


class VerticalFoldInstruction(defaults.Instruction):

    def execute(self, system_state, additional_parameters=dict()):
        points_right = {point for point in system_state['points'] if point[0] > self.instruction_parameters['value']}
        points_left = {point for point in system_state['points'] if point not in points_right}
        mirrored_points_right = {(2 * self.instruction_parameters['value'] - point[0], point[1]) for point in
                                 points_right}
        return set.union(points_left, mirrored_points_right)


if __name__ == '__main__':
    content = defaults.puzzle_input_now(2021, 13)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
