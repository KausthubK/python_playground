import os
import numpy as np
from matplotlib import pyplot as plt

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

    fig1 = plt.figure(1)
    fig1.set_size_inches(18.5, 10.5)
    fig1.suptitle('Concatenated Images L')

    fig2 = plt.figure(2)
    fig2.set_size_inches(18.5, 10.5)
    fig2.suptitle('Concatenated Images R')

    for i in range(6):
        if i%2 == 0:
            plt.figure(1)
            plt.imshow(np.asarray(img1))
            plt.draw()
            plt.figure(2)
            plt.imshow(np.asarray(img2))
            plt.draw()
        else:
            plt.figure(1)
            plt.imshow(np.asarray(img2))
            plt.draw()
            plt.figure(2)
            plt.imshow(np.asarray(img1))
            plt.draw()
        plt.pause(2) # pause how many seconds
    plt.close()


def concatenate_images_h(im_list):
    total_h = max([im.height for im in im_list])
    print(total_h)
    total_w = sum([im.width for im in im_list])
    print(total_w)
    cim = Image.new('RGB', (total_w, total_h))
    for idx, im in enumerate(im_list):
        cim.paste(im, (idx*im.width, 0))
    return cim


if __name__ == '__main__':
    main()
