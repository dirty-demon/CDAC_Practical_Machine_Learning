import cv2
import numpy as np


def resize_image():
    img = cv2.imread('./messi5.jpg')

    # get original image width and height
    (h, w, ch) = img.shape
    print(img.shape)

    # resize the image
    img_big = cv2.resize(img, (w * 4, h * 4))
    img_small = cv2.resize(img, (w - 100, h - 100))
    img_thumbnail = cv2.resize(img, (100, 100))

    # show the image
    cv2.imshow('messi', img)
    cv2.imshow('messi-bigger', img_big)
    cv2.imshow('messi-small', img_small)
    cv2.imshow('messi-thumb', img_thumbnail)

    # save the image
    cv2.imwrite("./messi5-bigger.jpg", img_big)
    cv2.imwrite("./messi5-thumb.jpg", img_thumbnail)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# resize_image()





def rotate_image():
    img = cv2.imread('./messi5.jpg')

    # get original image width and height
    (h, w, ch) = img.shape
    print(img.shape)

    # find the center
    # center = (w // 2, h // 2)
    center = (0, 0)

    # get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, 20, 1)

    # rotate the image
    img_rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

    # show the image
    cv2.imshow('messi', img)
    cv2.imshow('messi-rotated', img_rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# rotate_image()



def translate_image():
    img = cv2.imread('./messi5.jpg')

    # get original image width and height
    (h, w, ch) = img.shape
    print(img.shape)

    # get the translation matrix
    translation_matrix = np.array([[1, 0, 50], [0, 1, 50]], dtype=np.float32)

    # rotate the image
    img_rotated = cv2.warpAffine(img, translation_matrix, (w, h))

    # show the image
    cv2.imshow('messi', img)
    cv2.imshow('messi-rotated', img_rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


translate_image()
