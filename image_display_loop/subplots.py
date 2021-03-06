import os
import numpy as np
from matplotlib import pyplot as plt
from colorama import Fore

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

    fig, (ax1, ax2) = plt.subplots(2)
    fig.set_size_inches(18.5, 10.5)
    fig.suptitle('Concatenated Images')
    ax1.set_title('Left')
    ax2.set_title('Right')

    for i in range(6):
        print(Fore.LIGHTYELLOW_EX + "Be aware... plt.imshow() will add an image above the "
                                  + "previous data on the figure but WILL NOT CLEAR the "
                                  + "pre-existing data - that behaves effectively like a memory"
                                  + " leak and each loop will be slower than the last"
                                  + Fore.RESET)
        if i%2 == 0:
            ax1.imshow(np.asarray(img1))
            ax2.imshow(np.asarray(img2))
            plt.draw()
        else:
            ax1.imshow(np.asarray(img2))
            ax2.imshow(np.asarray(img1))
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
