import cv2
import numpy as np


# capture the video source
capture = cv2.VideoCapture(1)

# create the classifier
classifier = cv2.CascadeClassifier('./classifier_eye.xml')

while capture.isOpened():
    # capture the frame per second
    ret, frame = capture.read()

    # detect the face if any from the image/frame
    features = classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=15)

    # highlight the faces
    for (x, y, w, h) in features:

        # highlight the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

        # blur the feature
        # feature = frame[y: y + h, x: x + w].copy()
        # feature_blur = cv2.blur(feature, (100, 100))
        # frame[y: y + h, x: x + w] = feature_blur

    # show the image on the screen
    cv2.imshow('frame', frame)

    # check if user presses key 'q'
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


# release the video source
capture.release()

# destroy all windows
cv2.destroyAllWindows()
