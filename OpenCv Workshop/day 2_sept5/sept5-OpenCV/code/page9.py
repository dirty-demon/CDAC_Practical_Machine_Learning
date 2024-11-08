import cv2
import numpy as np


def function1():
    img = cv2.imread('./images/someshapes.jpg')

    # get the binary image
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)

    cv2.imshow('original', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    img = cv2.imread('./images/someshapes.jpg')

    # binary conversion
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,)

    # highlight / draw the contours
    for contour in contours:

        # draw every contour
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 5)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function2()


def function3():
    img = cv2.imread('./images/someshapes.jpg')

    # binary conversion
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,)

    index = 0

    # highlight / draw the contours
    for contour in contours:

        # find the bounding rect
        (x, y, w, h) = cv2.boundingRect(contour)

        # draw the rectangle for the bounding rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

        # crop the contour
        img_contour = img[y: y + h, x: x + w]
        cv2.imshow(f"shape: {index + 1}", img_contour)

        # write the contour into a file
        cv2.imwrite(f"images/shapes/shape_{index + 1}.png", img_contour)

        index += 1

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function3()


def function4():
    img = cv2.imread('./images/someshapes.jpg')

    # binary conversion
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,)

    # highlight / draw the contours
    for contour in contours:

        # find the bounding rect
        (x, y, w, h) = cv2.boundingRect(contour)

        # draw the rectangle for the bounding rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

        # approximate poly dp for finding the number of edges
        approximate_edges = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # print(f"no of edges = {len(approximate_edges)}")

        edges = len(approximate_edges)
        shape = ''
        if edges == 3:
            shape = 'triangle'
        elif edges == 4:
            if w == h:
                shape = 'square'
            else:
                shape = 'rectangle'
        elif edges == 10:
            shape = 'star'
        elif edges > 10:
            shape = 'circle'

        print(f"shape = {shape}")

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


function4()