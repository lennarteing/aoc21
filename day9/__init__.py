import matplotlib
import skimage
import cv2
import numpy as np


def solve_part_one(lines):
    numbers = format_input(lines)
    padded_numbers = np.pad(numbers, 1, constant_values=10)
    convolution_kernel = np.array([[0, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 0]])
    convoluted_image = cv2.filter2D(padded_numbers, -1, convolution_kernel)
    draw_image(convoluted_image)


def solve_part_two(lines):
    pass


def format_input(lines):
    return np.array([list(map(lambda x: int(x), list(line))) for line in lines], dtype=np.float)


def draw_image(image):
    skimage.io.imshow(image)
    matplotlib.pyplot.show()
