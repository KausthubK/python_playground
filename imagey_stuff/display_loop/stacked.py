import os
import numpy as np
from matplotlib import pyplot as plt
from colorama import Fore
import cv2
from datetime import datetime as dt
from PIL import Image

def main():
    image_size = (1000,1000)
    images1 = []
    images2 = []
    
    images1.append(Image.new('RGB', image_size, (255,255,255)))
    images1.append(Image.new('RGB', image_size, (255,0,0)))
    
    images2.append(Image.new('RGB', image_size, (0,255,0)))
    images2.append(Image.new('RGB', image_size, (0,0,255)))

    img1 = concatenate_images_h(im_list=images1)
    img2 = concatenate_images_h(im_list=images2)

    cv2.namedWindow("Stacked Image", cv2.WINDOW_NORMAL)  # this bit allows the frame to be resizeable
    for i in range(10):
        if i%2 == 0:
            img_stacked = concatenate_images_v([img1, img2])
        else:
            img_stacked = concatenate_images_v([img2, img1])
        print(Fore.CYAN + "[{} | stacked.py]".format(str(dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S.%f')[:-1]))
                        + " Displaying stack {}".format(i)
                        + Fore.RESET)                        
        cv2.imshow("Stacked Image", np.asarray(img_stacked))
        cv2.waitKey(1000)


## Concatenation functions for PIL Images - a similar thing can be done with np.stack if you're using the images as numpy arrays.
def concatenate_images_h(im_list):
    """
    Concatenates images horizontally cornered to the max height and the sum of the widths.
    
    Args:
        im_list (list): list of PIL.Image objects
    
    Returns:
        PIL.Image object
    """
    total_h = max([im.height for im in im_list])
    total_w = sum([im.width for im in im_list])
    cim = Image.new('RGB', (total_w, total_h))
    for idx, im in enumerate(im_list):
        cim.paste(im, (idx*im.width, 0))
    return cim

def concatenate_images_v(im_list):
    """
    Concatenates images vertically cornered to the sum of the heights and the max width.
    
    Args:
        im_list (list): list of PIL.Image objects
    
    Returns:
        PIL.Image object
    """
    total_h = sum([im.height for im in im_list])
    total_w = max([im.width for im in im_list])
    cim = Image.new('RGB', (total_w, total_h))
    for idx, im in enumerate(im_list):
        cim.paste(im, (0, idx*im.height))
    return cim


if __name__ == '__main__':
    main()
