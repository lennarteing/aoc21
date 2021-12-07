import numpy as np


def solve_part_one(lines):
    # Format line as beginning x, beginning y -> end x, end y
    # Only consider lines where x1 == x2 or y1==y2

    lines = [format_line(line) for line in lines]
    horizontal_lines = [(start, end) for start, end in lines if start[1] == end[1]]
    vertical_lines = [(start, end) for start, end in lines if start[0] == end[0]]
    point_map = {}
    for line in horizontal_lines:
        point_map = draw_line(line, point_map)
    for line in vertical_lines:
        point_map = draw_line(line, point_map)
    intersection_points = {point: num for point, num in point_map.items() if num > 1}
    return len(intersection_points)


def solve_part_two(lines):
    pass


def format_line(line):
    start, end = line.split(" -> ")
    x1, y1 = int(start.split(',')[0]), int(start.split(',')[1])
    x2, y2 = int(end.split(',')[0]), int(end.split(',')[1])
    start = x1, y1
    end = x2, y2
    return start, end


def draw_line(line, point_map):
    points = points_on_line(line)
    for point in points:
        point_map = draw_point(point, point_map)
    return point_map


def draw_point(point, point_map):
    if point not in point_map:
        point_map[point] = 0
    point_map[point] += 1
    return point_map


def points_on_line(line):
    points = []
    (x1, y1), (x2, y2) = line
    if x1 != x2:
        slope = (y2 - y1) / ((x2 - x1))
        for x in range(x1, x2 + 1):
            points.append((x, round(slope * x + y1)))
    else:
        for y in range(y1, y2 + 1):
            points.append((x1, y))
    return points
