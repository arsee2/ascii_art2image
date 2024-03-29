# ascii_art2image

This repository proposes two approaches to converting ASCII art into images (in common sense).
To run this project locally you should download  [weights](https://drive.google.com/file/d/1FJ_AnUD9Nd6noHf8HZNeEpgKpepx1GYc/view?usp=sharing).

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

### Dataset
You can use dataset for colorization which are used in initial github or as we you use dataset for art from kaggle<a href="https://www.kaggle.com/c/painter-by-numbers" title="link">
Art dataset </a>. We took trained model and train it on art dataset. therefore transfer learning was used.


## Second Model

The second approach renders an ASCII image and tries to connect unconnected image parts in order to obtain contours of the image(by means of PIX2PIX).
Using these contours it tires to reconstruct to a real object using PIX2PIX network.

### Implementation 
In order to obtain contours from ascii image, we trained Pix2Pix model that was taken from [link](https://github.com/affinelayer/pix2pix-tensorflow). We trained it on the following dataset: [link](https://github.com/OsciiArt/DeepAA/tree/master/sample%20images) which 
consists of 23 pair of images (original,ascii image).


In order to real object from contours, we trained Pix2Pix model that was taken from [link](https://github.com/affinelayer/pix2pix-tensorflow). We trained it on the following dataset: [link](https://github.com/mtli/PhotoSketch) which 
consists of contours and original images.

to run code use following comand : 

python main.py --model model2 --input_file input.txt

It will take txt file and produce result to /output directory


To run for input.txt you can use command :

python main.py --model model2

