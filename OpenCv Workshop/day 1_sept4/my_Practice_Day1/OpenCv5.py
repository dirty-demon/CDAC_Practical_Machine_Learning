import cv2
import numpy as np


def draw_lines():
    # create a black image (canvas)
    img = np.zeros((400, 400, 3), dtype=np.uint8)

    # draw a line
    cv2.line(img, (50, 50), (200, 50), (0, 255, 255), 1)
    cv2.line(img, (50, 100), (200, 100), (0, 255, 255), 5)
    cv2.line(img, (50, 150), (200, 150), (0, 255, 255), 10)

    # show the image
    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw_lines()


def draw_arrows():
    # create a black image (canvas)
    img = np.zeros((400, 400, 3), dtype=np.uint8)

    # draw arrows
    cv2.arrowedLine(img, (50, 50), (200, 50), (0, 255, 255), 1, cv2.LINE_4)
    cv2.arrowedLine(img, (50, 100), (200, 100), (0, 255, 255), 5, cv2.LINE_8)
    cv2.arrowedLine(img, (50, 150), (200, 150), (0, 0, 255), 10, cv2.LINE_8)

    # show the image
    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# draw_arrows()



def draw_rectangles():
    # create a black image (canvas)
    img = np.zeros((400, 400, 3), dtype=np.uint8)

    # draw arrows
    cv2.rectangle(img, (50, 50), (150, 100), (0, 255, 255), 1)
    cv2.rectangle(img, (50, 150), (150, 200), (0, 0, 255), 5)

    # show the image
    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# draw_rectangles()




def highlight_face():
    # read the image
    img = cv2.imread('./messi5.jpg')

    # highlight face with a rectangle
    cv2.rectangle(img, (190, 50), (280, 150), (0, 255, 255), 2)

    # highlight the football
    cv2.rectangle(img, (330, 280), (400, 340), (0, 0, 255), 2)

    # show the image
    cv2.imshow('messi', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# highlight_face()



def draw_circles():
    # create a black image (canvas)
    img = np.zeros((400, 400, 3), dtype=np.uint8)

    # draw arrows
    cv2.circle(img, (100, 100), 50, (0, 255, 255), 2)
    cv2.circle(img, (200, 200), 50, (0, 0, 255), -1)

    # show the image
    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# draw_circles()






def draw_texts():
    # create a black image (canvas)
    img = np.zeros((400, 500, 3), dtype=np.uint8)

    # draw texts
    cv2.putText(img, "welcome to OpenCV", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(img, "welcome to OpenCV", (30, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.5, (0, 255, 255), 2)

    # show the image
    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


draw_texts()

