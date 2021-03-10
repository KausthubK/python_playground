import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_dir = './raccoons'
images = [ Image.open(os.path.join(image_dir, f)) for f in os.listdir(image_dir)]
print(len(images))

plt.imshow(np.asarray(images[0]))
plt.draw()
plt.pause(5) # pause how many seconds
plt.close()