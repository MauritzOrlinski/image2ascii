from PIL import Image
import numpy as np


def rgb_to_brightness(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])


def get_image(path):
    image = Image.open(path)
    image = np.asarray(image)
    image_brightness = rgb_to_brightness(image)
    return image, image_brightness
