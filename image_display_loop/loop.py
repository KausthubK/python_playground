import os
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image

image_dir = './raccoons'
images = [ Image.open(os.path.join(image_dir, f)) for f in os.listdir(image_dir)]
print(len(images))

fig1 = plt.figure(1)
fig1.suptitle('blah')

fig2 = plt.figure(2)
fig2.suptitle('flooh')

for img in images:
    plt.figure(1)
    plt.imshow(np.asarray(img))
    plt.draw()
    plt.figure(2)
    plt.imshow(np.asarray(img))
    plt.pause(2) # pause how many seconds
plt.close()
