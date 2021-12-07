import numpy as np


def solve_part_one(lines):
    numbers, boards = format_input(lines)
    for num in numbers:
        for board in boards:
            board.mark(num)
            if board.is_won():
                return board.score(num)


def solve_part_two(lines):
    numbers, boards = format_input(lines)
    last_won_board_score = 0
    for num in numbers:
        for board in boards:
            if not board.is_marked_as_won():
                board.mark(num)
                if board.is_won():
                    board.mark_as_won()
                    last_won_board_score = board.score(num)
    return last_won_board_score


def format_input(lines, subdivisions=5):
    numbers = np.array([int(x) for x in lines[0].split(',')])
    boards = [line for line in lines[1:] if line != '']
    boards = np.array([str.split(line) for line in boards])
    boards = boards.astype(np.int)
    boards = np.array([Board(boards[x:x + subdivisions]) for x in range(0, len(boards), subdivisions)])
    return numbers, boards


class Board:

    def __init__(self, board_cell_values):
        self.board_cell_values = board_cell_values
        self.rotated_view = np.rot90(board_cell_values)
        self.marked_as_won = False

    def mark(self, value):
        self.board_cell_values[self.board_cell_values == value] = 0

    def score(self, last_value):
        return np.sum(self.board_cell_values) * last_value

    def is_won(self):
        horizontals = np.array([not np.any(line) for line in self.board_cell_values])
        verticals = np.array([not np.any(line) for line in self.rotated_view])
        return np.any(horizontals) or np.any(verticals)

    def is_marked_as_won(self):
        return self.marked_as_won

    def mark_as_won(self):
        self.marked_as_won = True

    def __str__(self):
        return str(self.board_cell_values)

