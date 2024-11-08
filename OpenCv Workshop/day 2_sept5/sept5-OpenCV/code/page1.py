import cv2
import numpy as np


def function1():
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

    cv2.imshow('original', img)
    cv2.imshow('corrected', img_corrected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./images/wrong_perspective.png')

    # get the old points which are having perspective issue
    old_points = np.array([[35, 254], [345, 150], [290, 740], [630, 520]], dtype=np.float32)

    # create the new set of points
    new_points = np.array([[0, 0], [420, 0], [0, 594], [420, 594]], dtype=np.float32)

    # create the transformation matrix
    matrix = cv2.getPerspectiveTransform(old_points, new_points)

    # correct the perspective issue
    img_corrected = cv2.warpPerspective(img, matrix, (420, 594))

    cv2.imshow('original', img)
    cv2.imshow('corrected', img_corrected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function2()