# ascii_art2image

This repository proposes two approaches to converting ASCII art into images (in common sense).

## First Model 
The first approach decodes each character into pixel by its intensity, i.e. how much space a pixel takes up.   
After, it colorizes obtained the gray-scale image.

to run code use following comand : 

python main.py --model model1 --input_file input.txt

It will take txt file and produce result to /output directory


To run for input.txt you can use command :

python main.py --model model1


### Implementation
The approach of decoding from image to ascii and from ascii to image contains in pic_to_ascii.py


The colorization contains in colorizer22 folder.

It uses realization from  <a href="https://github.com/Armour/Automatic-Image-Colorization" title="link">
Automatic-Image-Colorization </a>

## Second Model

The second approach renders an ASCII image and tries to connect unconnected image parts in order to obtain contours of the image(by means of PIX2PIX).
Using these contours it tires to reconstruct to a real object using PIX2PIX network.
