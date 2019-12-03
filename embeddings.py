from constants import TEXT_WIDTH, TEXT_HEIGHT, RENDER_WIDTH, RENDER_HEIGHT
# from PIL import _imaging
from utils import from_string_to_lines,resize_embedding
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import pickle
import numpy as np


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

    embedding = np.array([np.array([to_intesity(c) for c in line]) for line in ascii_text])
    return resize_embedding(embedding)


def embed_by_ascii(string):
    '''
    more often characters should have lower values
    :param symbol_matrix: [[char]]
    :return:
    '''
    ascii_text = from_string_to_lines(string)
    embedding = np.array([np.array([(ord(c)/128) for c in line]) for line in ascii_text])

    return resize_embedding(embedding)



def embed_by_render(string):
    width = 1024
    height = 800
    ascci_width = TEXT_WIDTH
    ascii_height = TEXT_HEIGHT
    dx = width / ascci_width
    dy = height / ascii_height
    image = Image.new("RGBA", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 18)
    ascii_text = from_string_to_lines(string)
    for i, line in enumerate(ascii_text):
        for j, ch in enumerate(line):
            draw.text((j * dx, i * dy), ch, (0, 0, 0), font=font)
    img_resized = image.resize((RENDER_WIDTH, RENDER_HEIGHT), Image.BICUBIC)
    gray = np.mean(img_resized, axis=2)
    return gray


ascii_text = ["___________                        _________                      __  .__    .__                ",
"\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____  ",
"  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\ " ,
"  |    |  \___  ||  |_> >  ___/   /        (  <_9 )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  >" ,
"  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  / ",
"          \/     |__|        \/          \/             \/     \/          \/        \//_____/  ",]

ascii_text = ('\n'.join([a for a in ascii_text]))

import time
t0 = time.time()
for i in range(100):
    embed_by_render(ascii_text)
t1 = time.time()
print(t1-t0)