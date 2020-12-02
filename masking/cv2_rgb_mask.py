import cv2
import numpy as np
import matplotlib.pyplot as plt


classes_bgr = {
    'BLD': (186, 61, 184),
    'GRD': (255, 255, 255),
    'MMS': (39, 127, 255),
    'RDS': (27, 0, 136),
    'TRS': (69, 209, 14),
    'WTR': (204, 72, 63)
    }

im_bgr = cv2.imread('image.png', 1)
gt_bgr = cv2.imread('mask.png', 1)
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
gt_rgb = cv2.cvtColor(gt_bgr, cv2.COLOR_BGR2RGB)

for c in classes_bgr:
    print(c)
    plt.imshow(im_rgb)
    plt.show()
    plt.imshow(gt_rgb)
    plt.show()

    gt_r = gt_rgb[:, :, 0]
    gt_g = gt_rgb[:, :, 1]
    gt_b = gt_rgb[:, :, 2]

    mask_r = (gt_r == classes_bgr[c][2])
    mask_g = (gt_g == classes_bgr[c][1])
    mask_b = (gt_b == classes_bgr[c][0])

    gb_mask = np.logical_and(mask_g, mask_b)
    rgb_mask = np.logical_and(mask_r, gb_mask)
    rgb_mask_float = rgb_mask * 255.0
    plt.imshow(rgb_mask_float, cmap='gray')
    plt.show()

