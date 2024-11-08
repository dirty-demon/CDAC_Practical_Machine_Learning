import cv2
import numpy as np


img = cv2.imread('./images/messi5.jpg')

# create kernel for sharpening the image
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

# apply the kernel on the image
img_sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow('original', img)
cv2.imshow('sharpened', img_sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()