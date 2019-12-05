# ascii_art2image

This repository proposes two approaches to converting ASCII art into images (in common sense).

## First Model 
The first approach decodes each character into pixel by its intensity, i.e. how much space a pixel takes up.   
After, it colorizes obtained the gray-scale image.

## Second Model

The second approach renders an ASCII image and tries to connect unconnected image parts in order to obtain contours of the image(by means of PIX2PIX).
Using these contours it tires to reconstruct to a real object using PIX2PIX network.
