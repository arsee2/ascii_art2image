from constants import TEXT_WIDTH, TEXT_HEIGHT
import cv2
import numpy as np

def resize_image(img):
    '''
    :param img: original image
    :return: (TEXT_WIDTHxTEXT_HEIGHT) image
    '''
    return resized_img


def from_string_to_lines(string):
    return [s for s in string.splitlines()]


def resize_embedding(embedding):

    return cv2.resize(embedding, dsize=(TEXT_WIDTH, TEXT_HEIGHT), interpolation=cv2.INTER_CUBIC)

