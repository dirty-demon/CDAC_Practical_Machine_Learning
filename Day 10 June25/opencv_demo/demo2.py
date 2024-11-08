import numpy as np
import cv2

# read file
image = cv2.imread('human.png')
print(image.shape)

# convert the image into gray scale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)

# show the image
cv2.imshow('image', image)
cv2.waitKey(0)
