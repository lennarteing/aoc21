import re
from abc import abstractmethod, ABC

import numpy as np


def solve_part_one(lines):
    points, fold_instructions = format_input(lines)
    points = fold_instructions[0].execute_fold(points)
    return len(points)


def solve_part_two(lines):
    points, fold_instructions = format_input(lines)
    for instruction in fold_instructions:
        points = instruction.execute_fold(points)
    max_x = max(points, key=lambda point: point[0])[0]
    max_y = max(points, key=lambda point: point[1])[1]
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
    instructions = [HorizontalFoldInstruction(int(match.group('value'))) if match.group('direction') == 'y'
                    else VerticalFoldInstruction(int(match.group('value'))) for
                    match in instruction_line_matches]
    return points, instructions


class FoldInstruction(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def execute_fold(self, points):
        pass


class HorizontalFoldInstruction(FoldInstruction):

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "Horizontal fold at: " + str(self.value)

    def execute_fold(self, points):
        points_below = {point for point in points if point[1] > self.value}
        points_above = {point for point in points if point not in points_below}
        mirrored_points_below = {(point[0], self.value - (point[1] - self.value)) for point in points_below}
        return set.union(points_above, mirrored_points_below)


class VerticalFoldInstruction(FoldInstruction):

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "Vertical fold at: " + str(self.value)

    def execute_fold(self, points):
        points_right = {point for point in points if point[0] > self.value}
        points_left = {point for point in points if point not in points_right}
        mirrored_points_right = {(self.value - (point[0] - self.value), point[1]) for point in points_right}
        return set.union(points_left, mirrored_points_right)
