# from package installation folder of pycharm install "Opencv-python"

# import opencv
import cv2

# read the file
img = cv2.imread('./messi5.jpg')

# inspect the img
print(img)
print(f"data type of img = {type(img)}")
print(f"shape = {img.shape}")

(h, w, ch) = img.shape
print(f"width: {w}, height: {h}, #channels: {ch}, resolution: {w}x{h}")
print(f"dimensions = {img.ndim}")

# render file in a window
cv2.imshow("messi", img)

# wait for 5 seconds
# cv2.waitKey(5000)

# wait till use presses a key
cv2.waitKey(0)

# close the rendering window
# destroy the rendering window
cv2.destroyAllWindows()

