from utils import load_file
from embeddings import embed_by_render
import cv2
import os
import argparse
import numpy as np
import shutil
from pic_to_ascii import get_from_ascii

parser = argparse.ArgumentParser(description='Generate images from text file.')

parser.add_argument("--model", default='model2', choices=["model1", "model2"], help="One of the 2 models")
parser.add_argument("--input_file", default='input.txt', required=False, help='path to text file')
parser.add_argument("--output_file", default='output/', required=False, help='path to output directory')
a = parser.parse_args()

text = load_file(a.input_file)

assert (a.model == 'model1' or a.model == 'model2')
assert not (text == "")


def run_ascii_to_edge():
    os.system(
        "python pix2pix.py --input_dir temp\\ascii_image\\ --output_dir temp\\edged\\ --mode test --checkpoint ascii2edges\\")

def run_edges_to_pict():
    os.system(
        "python pix2pix.py --input_dir temp\\edged\\ --output_dir temp\\image\\ --mode test --checkpoint edges2img\\")

def colorize():
    os.chdir('colorizer22/git/')
    print(os.listdir("."))
    os.system("python test.py")
    os.chdir('../../')



if a.model == 'model2':
    img = embed_by_render(text)

    scale_percent = 35  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img,dim)
    img = np.array(img)
    img.astype(int)
    img[img<128]=0
    img[img > 128] = 255
    img = np.array([np.array(row.astype(int)) for row in img])



    img = np.stack((img,)*3, axis=-1)
    cv2.imwrite('temp\\ascii_image\\ascii_image.jpg', cv2.hconcat([img, img]))
    cv2.imwrite('output\\original.jpg', img)
    shutil.rmtree('temp\\edged\\')
    os.mkdir('temp\\edged\\')

    run_ascii_to_edge()


    edged_img = cv2.imread("temp\\edged\\images\\ascii_image-outputs.png")
    edged_img = cv2.resize(edged_img,dim)
    cv2.imwrite('temp\\edged\\edged.jpg', cv2.hconcat([edged_img, edged_img]))
    cv2.imwrite('output\\edged.jpg', edged_img)
    run_edges_to_pict()

    cv2.imwrite("colorizer22/git/test2014/a.jpeg", edged_img)
    shutil.rmtree("colorizer22/git/summary/")

    colorize()



    gen_image = cv2.imread("temp\\image\\images\\edged-outputs.png")
    gen_image = cv2.resize(gen_image, dim)
    cv2.imwrite('output\\generated.jpg', gen_image)
else:
    shutil.rmtree("colorizer22/git/summary/")
    img = get_from_ascii(a.input_file)
    res = cv2.resize(img, (256, 256))

    res = cv2.cvtColor(res,cv2.COLOR_GRAY2RGB)
    print(os.getcwd())
    cv2.imwrite("colorizer22/git/test2014/a.jpeg", res)

    colorize()






