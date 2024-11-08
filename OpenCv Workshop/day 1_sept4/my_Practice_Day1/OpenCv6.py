import cv2


def split_channels():
    # read the image
    img = cv2.imread('./messi5.jpg')

    # split the channels
    (b, g, r) = cv2.split(img)
    # print(f"blue channel: {b}")


    # change the intensity of the channels
    img_red = cv2.merge([b, g, r + 100])
    img_green = cv2.merge([b, g + 100, r])
    img_blue = cv2.merge([b + 100, g, r])

    # show the image
    cv2.imshow('messi', img)
    cv2.imshow('messi-red', img_red)
    cv2.imshow('messi-green', img_green)
    cv2.imshow('messi-blue', img_blue)

    # show different channel images
    # cv2.imshow('messi-red', r)
    # cv2.imshow('messi-green', g)
    # cv2.imshow('messi-blue', b)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


# split_channels()




def crop_image():
    # read the image
    img = cv2.imread('./messi5.jpg')

    # face
    img_face = img[50:150, 200:280]

    # ball
    # (330, 280), (400, 340)
    img_ball = img[280:340, 330:400]

    # show the image
    cv2.imshow('messi', img)
    cv2.imshow('messi-face', img_face)
    cv2.imshow('messi-ball', img_ball)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# crop_image()


def crop_copy_ball():
    # read the image
    img = cv2.imread('./messi5.jpg')

    # ball
    # (330, 280), (400, 340)
    img_ball = img[280:340, 330:400].copy()

    # copy the ball to another location in the original image
    # (120, 270), (190, 330)
    img[270:330, 120:190] = img_ball

    # show the image
    cv2.imshow('messi', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# crop_copy_ball()



def crop_copy_face():
    # read the image
    img = cv2.imread('./messi5.jpg')

    # face
    img_face = img[50:150, 200:280].copy()

    # blurr the face
    img_face_blurr = cv2.blur(img_face, (20, 20))

    # put the same face back
    img[50:150, 200:280] = img_face_blurr

    # show the image
    cv2.imshow('messi', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


crop_copy_face()