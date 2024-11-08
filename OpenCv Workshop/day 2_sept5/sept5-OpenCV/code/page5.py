import cv2
import numpy as np


def function1():
    img = cv2.imread('./images/messi5.jpg')

    # create a matrix (image)
    matrix = np.ones(img.shape, dtype=np.uint8) * 150

    # add two images
    image_result = cv2.add(img, matrix)

    cv2.imshow('original', img)
    cv2.imshow('matrix', matrix)
    cv2.imshow('result', image_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./images/messi5.jpg')
    # print(img)

    # create a matrix (image)
    matrix = np.ones(img.shape, dtype=np.uint8) * 100
    # print(matrix)

    # add two images
    image_result = cv2.subtract(img, matrix)
    # print(image_result)

    cv2.imshow('original', img)
    cv2.imshow('matrix', matrix)
    cv2.imshow('result', image_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function2()