import cv2
import numpy as np


def function1():
    img_1 = cv2.imread('./images/messi5.jpg')
    img_2 = cv2.imread('./images/opencv-logo-white.png')

    # get the shape of the first image
    (h, w, ch) = img_1.shape

    # resize the second image
    img_2_resized = cv2.resize(img_2, (w, h))

    # blend two images
    img_result = cv2.add(img_1, img_2_resized)

    cv2.imshow('original-1', img_1)
    cv2.imshow('original-2', img_2)
    cv2.imshow('result', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img_1 = cv2.imread('./images/messi5.jpg')
    # img_2 = cv2.imread('./images/opencv-logo-white.png')
    img_2 = cv2.imread('./images/blending_image.png')

    # get the shape of the first image
    (h, w, ch) = img_1.shape
    print(img_1.shape)

    # resize the second image
    img_2_resized = cv2.resize(img_2, (w, h))

    # blend two images
    img_result = cv2.addWeighted(img_1, 0.8, img_2_resized, 0.5, 0.5)

    cv2.imshow('original-1', img_1)
    cv2.imshow('original-2', img_2)
    cv2.imshow('result', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function2()


def function3():
    capture = cv2.VideoCapture(1)
    img_2 = cv2.imread('./images/blending_image.png')

    while capture.isOpened():
        ret, frame = capture.read()

        # get the shape of the first image
        (h, w, ch) = frame.shape

        # resize the second image
        img_2_resized = cv2.resize(img_2, (w, h))

        # blend two images
        img_result = cv2.addWeighted(frame, 0.8, img_2_resized, 0.5, 0.5)

        cv2.imshow('original', frame)
        cv2.imshow('canny', img_result)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


# function3()


def function4():
    img_1 = cv2.imread('./images/messi5.jpg')

    # blend two images
    img_result = cv2.bitwise_not(img_1)

    cv2.imshow('original-1', img_1)
    cv2.imshow('result', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


function4()
