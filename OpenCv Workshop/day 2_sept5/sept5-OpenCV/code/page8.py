import numpy as np
import cv2


def function1():
    img = cv2.imread('./images/sudoku.jpg')

    # convert the image into grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold image
    ret, img_threshold_1 = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
    ret, img_threshold_2 = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow('original', img)
    cv2.imshow('gray', img_gray)
    cv2.imshow('binary-1', img_threshold_1)
    cv2.imshow('binary-2', img_threshold_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./images/scan.jpg')

    # get the old points which are having perspective issue
    # top-left, top-right, bottom-left, bottom-right
    old_points = np.array([[320, 15], [700, 215], [85, 610], [530, 780]], dtype=np.float32)

    # create the new set of points
    new_points = np.array([[0, 0], [420, 0], [0, 594], [420, 594]], dtype=np.float32)

    # create the transformation matrix
    matrix = cv2.getPerspectiveTransform(old_points, new_points)

    # correct the perspective issue
    img_corrected = cv2.warpPerspective(img, matrix, (420, 594))

    # convert the image to gray scale
    img_gray = cv2.cvtColor(img_corrected, cv2.COLOR_BGR2GRAY)

    # threshold the image
    ret, img_threshold = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)
    print(img_threshold)

    cv2.imshow('original', img)
    cv2.imshow('corrected', img_corrected)
    cv2.imshow('gray', img_gray)
    cv2.imshow('threshold', img_threshold)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function2()