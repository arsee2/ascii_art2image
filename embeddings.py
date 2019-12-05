from constants import TEXT_WIDTH, TEXT_HEIGHT, RENDER_WIDTH, RENDER_HEIGHT
# from PIL import _imaging
from utils import from_string_to_lines, resize_embedding
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import pickle
import numpy as np
import cv2




def embed_by_intensity(string):
    '''
    :param symbol_matrix: [[char]]
    :return: [[float]]
    '''
    with open(r"embedding_weights\intensity_weights.pickle", "rb") as input_file:
        mapper = pickle.load(input_file)
    ascii_text = from_string_to_lines(string)

    def to_intesity(character):
        num = ord(character)
        if num in mapper:
            return mapper[num]
        else:
            return 1/2
    max_length = np.max([len(line) for line in ascii_text])
    embedding = np.array([([to_intesity(c) for c in line]+[0]*(max_length-len(line))) for line in ascii_text])
    return resize_embedding(embedding)


def embed_by_ascii(string):
    '''
    more often characters should have lower values
    :param symbol_matrix: [[char]]
    :return:
    '''
    ascii_text = from_string_to_lines(string)


    embedding = np.array([np.array([(ord(c) ) for c in line]) for line in ascii_text])

    return resize_embedding(embedding)


def embed_by_render(string):
    ascii_text = from_string_to_lines(string)
    width = 1024

    ascii_height = len(ascii_text)
    ascci_width = np.max([len(line) for line in ascii_text])
    ratio = ascci_width/ascii_height
    height = int(width/ratio)*2

    dx = width / ascci_width
    dy = height / ascii_height
    image = Image.new("RGBA", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", int(25/15/ascci_width*width))

    for i, line in enumerate(ascii_text):
        for j, ch in enumerate(line):
            ren_ch = ch if (ord(ch)<128) else ' '
            draw.text((j * dx, i * dy), ren_ch, (0, 0, 0), font=font)
    #img_resized = image.resize((RENDER_WIDTH, RENDER_HEIGHT), Image.BICUBIC)
    print (image)
    gray = (  np.asarray(image))
    gray = np.mean(gray, axis=2)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.erode(gray, kernel, iterations=2)

    return dilated

