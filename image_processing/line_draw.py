import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/soham1.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
