import numpy as np

brightness_to_char = [" ", ".", "'", ",", "-", "~", ":", "/", "=", "<", "C", "O", "1", "+", "*", "z", "#", "S", "$",
                      "8", "@"]


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


def make_text(image, width, height=None):
    text_array = []
    if width > image.shape[0]:
        width = image.shape[0]

    if height is None:
        height = int(width * image.shape[0] / image.shape[1])

    compressed_image = compress(image, width, height)
    for i in range(width):
        text_array.append([])
        for j in range(height):
            text_array[i].append(brightness_to_char[int(compressed_image[i][j] / 255 * (len(brightness_to_char) - 1))])

    text_for_terminal = ""
    text_to_file = ""
    for i in range(width):
        for j in range(height):
            text_for_terminal += text_array[i][j] 
            text_to_file += text_array[i][j]
        text_for_terminal += "\n"
        text_to_file += "\n"

    return text_for_terminal, text_to_file


def store_to_txt(text, path):
    with open(path, "w") as file:
        file.write(text)
