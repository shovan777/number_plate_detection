
"""Resize and convert imgs to greyscale."""
import os
from os.path import join
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
import cv2
import numpy as np
import sys

# print(len(sys.argv))
# check if data location is provided
if (len(sys.argv) < 2):
  print("give data dir")
  sys.exit(-1)

"""Initialize path and size variables."""
img_dir_path = sys.argv[1]
new_size_h = 512
new_size_w = 512

# get the paths of image into a list
img_paths = os.listdir(path=img_dir_path)
i = 1

# loop through the images
for img_path in img_paths:
    img_absolute_path = join(img_dir_path, img_path)
    new_img_path = join(img_dir_path, img_path)
    i = i + 1
    # read image
    img = cv2.imread(img_absolute_path)
    print(img_absolute_path)

    # convert to greyscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # resize
    img = cv2.resize(img, (new_size_w, new_size_h))
#     img = img.astype(np.float32)
#     img /= 255
#     save the image
    cv2.imwrite(new_img_path, img)
#     plt.imshow(plt.imread(img_absolute_path))
