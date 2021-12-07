from scipy.optimize import minimize

import numpy as np


def solve_part_one(lines):
    numbers = list(map(lambda x: int(x), lines[0].split(',')))
    x0 = (average(numbers),)
    minimum = minimize(fun=total_distance, x0=x0, args=(numbers,), method='Nelder-Mead')
    return round(minimum.fun);


def solve_part_two(lines):
    numbers = list(map(lambda x: int(x), lines[0].split(',')))
    x0 = (average(numbers),)
    minimum = minimize(fun=growing_distance, x0=x0, args=(numbers,), method='Nelder-Mead')
    return round(minimum.fun);


def total_distance(point, *args):
    return sum(map(lambda x: abs(point - x), args[0]))


def growing_distance(point, *args):
    return sum(map(lambda x: single_growing_distance(point, x), args[0]))


def single_growing_distance(x, y):
    distance = sum([_ for _ in range(int(np.round(abs(y - x) + 1)))])
    return distance


def average(numbers):
    return sum(numbers) / len(numbers)
