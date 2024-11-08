import cv2
import numpy as np


def function1():
    img = cv2.imread('./images/messi5.jpg')

    # detect the edges from the image
    img_canny = cv2.Canny(img, 255, 255)

    cv2.imshow('original', img)
    cv2.imshow('canny', img_canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    capture = cv2.VideoCapture(1)

    while capture.isOpened():
        ret, frame = capture.read()

        # detect the edges from the image
        frame_canny = cv2.Canny(frame, 150, 150)

        cv2.imshow('original', frame)
        cv2.imshow('canny', frame_canny)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


function2()