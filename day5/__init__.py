import matplotlib
import skimage
import numpy as np

import defaults


def solve_part_one(lines):
    # Format line as beginning x, beginning y -> end x, end y
    # Only consider lines where x1 == x2 or y1==y2

    lines = [format_line(line) for line in lines]
    line_map = np.zeros(shape=find_map_dimensions(lines))
    vertical_lines = [line for line in lines if line[1] == line[3]]
    horizontal_lines = [line for line in lines if line[0] == line[2]]
    add_lines_to_map(vertical_lines, line_map)
    add_lines_to_map(horizontal_lines, line_map)
    overlaps = line_map[line_map > 1]
    draw_map(line_map)
    return len(overlaps)


def solve_part_two(lines):
    lines = [format_line(line) for line in lines]
    line_map = np.zeros(shape=find_map_dimensions(lines))
    add_lines_to_map(lines, line_map)
    draw_map(line_map)
    overlaps = line_map[line_map > 1]
    return len(overlaps)


def add_lines_to_map(lines, line_map):
    for line in lines:
        x1, y1, x2, y2 = line
        rr, cc = skimage.draw.line(x1, y1, x2, y2)
        line_map[rr, cc] += 1
    return lines, line_map


def format_line(line):
    start, end = line.split(" -> ")
    x1, y1 = int(start.split(',')[0]), int(start.split(',')[1])
    x2, y2 = int(end.split(',')[0]), int(end.split(',')[1])
    return x1, y1, x2, y2


def find_map_dimensions(points):
    return np.max(points) + 1, np.max(points) + 1


def draw_map(line_map):
    skimage.io.imshow(line_map)
    matplotlib.pyplot.show()


if __name__ == '__main__':

    content = defaults.puzzle_input_now(2021, 5)

    part_one_solution = solve_part_one(content)
    part_two_solution = solve_part_two(content)

    print("The solution to part one is: " + str(part_one_solution))
    print("The solution to part two is: " + str(part_two_solution))
