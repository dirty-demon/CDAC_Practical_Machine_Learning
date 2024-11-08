import cv2
import numpy as np


def function1():
    img = cv2.imread('./images/opencv_inv.png')

    # get a kernel of size 5x5
    kernel = np.ones((5, 5), dtype=np.uint8)

    # apply the kernel using dilate function
    img_result = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('result', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./images/opencv_inv.png')

    # get a kernel of size 5x5
    kernel = np.ones((5, 5), dtype=np.uint8)

    # apply the kernel using dilate function
    img_result = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('result', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function2()
