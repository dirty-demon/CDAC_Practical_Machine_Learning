import numpy as np
import cv2

# read file
image = cv2.imread('human.png')
print(image)

# show the image
cv2.imshow('image', image)
cv2.waitKey(0)
