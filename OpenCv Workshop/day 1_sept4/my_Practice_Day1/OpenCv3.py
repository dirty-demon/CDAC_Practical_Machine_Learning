import cv2


def capture_one_frame():
    # capture/open the source
    capture = cv2.VideoCapture(0)

    # take a frame/photo from source
    ret, frame = capture.read()

    # render the image/frame
    cv2.imshow('frame', frame)

    # wait for user
    cv2.waitKey(0)

    # close the source
    capture.release()

    # destroy windows
    cv2.destroyAllWindows()


# capture_one_frame()


def capture_video():
    # capture/open the source
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        # take a frame/photo from source
        ret, frame = capture.read()

        # render the image/frame
        cv2.imshow('frame', frame)

        # wait for user to press q
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # close the source
    capture.release()

    # destroy windows
    cv2.destroyAllWindows()


capture_video()