import cv2
import numpy as np


def function1():
    img = cv2.imread('./messi5.jpg')

    # add blur in the image
    img_blurred = cv2.blur(img, (10, 10))

    cv2.imshow('original', img)
    cv2.imshow('blurred', img_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



# function1()


def function2():
    img = cv2.imread('./messi5.jpg')

    # create the blur matrix
    kernel = np.ones((10, 10), dtype=np.float) / 100

    # apply the matrix on the image
    img_blurred = cv2.filter2D(img, -1, kernel)

    cv2.imshow('original', img)
    cv2.imshow('blurred', img_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function2()
