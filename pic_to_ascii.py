# Python code to convert an image to ASCII image. 
# -*- coding: utf-8 -*-

import sys, random, argparse 
import numpy as np 
import math 
import cv2

from PIL import Image 
  
# gray scale level values from:  
# http://paulbourke.net/dataformats/asciiart/ 
  
# 70 levels of gray 
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
  
# 10 levels of gray 
gscale2 = '@%#*+=-:. '

vals = {}
for i in range(len(gscale1)):
    vals[gscale1[i]] = i * (255 / len(gscale1))
  
def getAverageL(image): 
  
    """ 
    Given PIL Image, return average value of grayscale value 
    """
    # get image as numpy array 
    im = np.array(image) 
  
    # get shape 
    w,h = im.shape 
  
    # get average 
    return np.average(im.reshape(w*h)) 


def pad_image(im):
    old_size = im.shape[:2] # old_size is in (height, width) format
    desired_size = max(old_size)
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [255, 255, 255]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)

    cv2.imshow("image", new_im)
    cv2.waitKey(0)


    return new_im
  
def covertImageToAscii(fileName, cols, rows, moreLevels): 
    """ 
    Given Image and dims (rows, cols) returns an m*n list of Images  
    """
    # declare globals 
    global gscale1, gscale2 
  
    # open image and convert to grayscale 
    image = Image.open(fileName).convert('L') 
  
    # store dimensions 
    W, H = image.size[0], image.size[1] 
    print("input image dims: %d x %d" % (W, H))
   
    # compute width of tile 
    w = W/cols 
  
    # compute tile height based on aspect ratio and scale 
    h = H/rows 
  
    # compute number of rows 
    rows = int(H/h) 
      
    print("cols: %d, rows: %d" % (cols, rows)) 
    print("tile dims: %d x %d" % (w, h)) 
  
    # check if image size is too small 
    if cols > W or rows > H: 
        print("Image too small for specified cols!") 
        exit(0) 
  
    # ascii image is a list of character strings 
    aimg = [] 
    # generate list of dimensions 
    for j in range(rows): 
        y1 = int(j*h) 
        y2 = int((j+1)*h) 
  
        # correct last tile 
        if j == rows-1: 
            y2 = H 
  
        # append an empty string 
        aimg.append("") 
  
        for i in range(cols): 
  
            # crop image to tile 
            x1 = int(i*w) 
            x2 = int((i+1)*w) 
  
            # correct last tile 
            if i == cols-1: 
                x2 = W 
  
            # crop image to extract tile 
            img = image.crop((x1, y1, x2, y2)) 
  
            # get average luminance 
            avg = int(getAverageL(img)) 
  
            # look up ascii char 
            if moreLevels: 
                gsval = gscale1[int((avg*69)/255)] 
            else: 
                gsval = gscale2[int((avg*9)/255)] 
  
            # append ascii char to string 
            aimg[j] += gsval 
      
    # return txt image 
    return aimg 
import numpy as np

def get_from_ascii(fileName):
    f = open(fileName,"r",encoding="utf-8")
    lines = f.readlines()
    n = len(lines)
    m = 0
    for i in range(n):
        m = max(m, len(lines[i]))
    vis = np.zeros((n, m), np.float32)
    vis[:,:] = 255

    for i in range(n):
        for j in range(len(lines[i])-1):
            try : 
                vis[i][j] = vals[lines[i][j]]
            except:
                vis[i][j] = 255/2
    im = np.array(vis, dtype=np.uint8)

    return im




def pic_main():
    text_size = 50

    img = cv2.imread("horne.png")
    img  = pad_image(img)
    #img = cv2.resize(img,(256,256))
    cv2.imwrite("temp.png",img)


    img = covertImageToAscii("temp.jpg",text_size,text_size,True)
    outFile = 'out.txt'
    # open file
    f = open(outFile, 'w')

    # write to file
    for row in img:
        f.write(row + '\n')
    # cleanup
    f.close()


    res = get_from_ascii(outFile)

    res = cv2.resize(res, (256,256))

    cv2.imwrite("res.png",res)




