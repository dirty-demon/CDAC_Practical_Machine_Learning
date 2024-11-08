import cv2


def convert_image_to_grayscale():
    img = cv2.imread('./messi5.jpg')

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # render original image
    cv2.imshow('messi-original', img)

    # render the gray scale image
    cv2.imshow('messi-grayscale', img_gray)

    # wait for user and destroy
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# convert_image_to_grayscale()


def convert_video_to_grayscale():
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        ret, img = capture.read()

        # convert the original frame to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # render original image
        cv2.imshow('original', img)

        # render the gray scale image
        cv2.imshow('grayscale', img_gray)

        # wait for user and destroy
        if cv2.waitKey(20) & 0xff == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


convert_video_to_grayscale()