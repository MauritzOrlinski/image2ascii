import numpy as np
import math

brightness_to_char = [" ", ".", "'", ",", "-", "~", ":", "/", "=", "<", "C", "O", "1", "+", "*", "z", "#", "S", "$",
                      "8", "@"]


def get_color(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, int(r), int(g), int(b))


def compress(image, width, height):
    (image_width, image_height) = image.shape
    width_ratio = image_width / width
    height_ratio = image_height / height

    average_brightness = []

    for i in range(width):
        average_brightness.append([])
        for j in range(height):
            average_brightness[i].append(np.average(image[int(i * width_ratio):int((i + 1) * width_ratio),
                                                    int(j * height_ratio):int((j + 1) * height_ratio)]))
    return np.array(average_brightness)


def compress_colors(image, width, height):
    (image_width, image_height, rgb) = image.shape
    width_ratio = image_width / width
    height_ratio = image_height / height

    average_brightness = []

    for i in range(width):
        average_brightness.append([])
        for j in range(height):
            average_brightness[i].append([])
            for k in range(3):
                average_brightness[i][j].append(np.average(image[int(i * width_ratio):int((i + 1) * width_ratio),
                                                           int(j * height_ratio):int((j + 1) * height_ratio),
                                                           k]))
    return np.array(average_brightness)


def make_text(image, image_brightness, width, height=None, colorful=True, extended_chars=0):
    text_array = []
    if width > image_brightness.shape[1]:
        width = image_brightness.shape[1]

    if height is None:
        height = int((width * image_brightness.shape[1] / image_brightness.shape[0]))

    compressed_image = compress(image_brightness, width, height)
    compressed_colors = compress_colors(image, width, height)
    for i in range(width):
        text_array.append([])
        for j in range(height):
            text_array[i].append(brightness_to_char[int(compressed_image[i][j] / 255 * (len(brightness_to_char) - 1))])

    text_for_terminal = ""
    text_to_file = ""
    for i in range(width):
        for j in range(height):
            if colorful:
                text_for_terminal += get_color(compressed_colors[i][j][0], compressed_colors[i][j][1],
                                               compressed_colors[i][j][2])
                for k in range(extended_chars + 1):
                    text_for_terminal += "#"
                    text_to_file += text_array[i][j]
            else:
                for k in range(extended_chars + 1):
                    text_for_terminal += text_array[i][j]
                    text_to_file += text_array[i][j]
        text_for_terminal += "\n"
        text_to_file += "\n"
    text_for_terminal += '\033[0m'
    return text_for_terminal, text_to_file


def store_to_txt(text, path):
    with open(path, "w") as file:
        file.write(text)
