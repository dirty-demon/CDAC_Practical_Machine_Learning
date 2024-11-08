import cv2

# capture/open the source
capture = cv2.VideoCapture(0)

# take a frame/photo from source
ret, frame = capture.read()

# render the image/frame
cv2.imshow('frame', frame)

# wait for user
cv2.waitKey(0)

capture.release()

# destroy windows
cv2.destroyAllWindows()

