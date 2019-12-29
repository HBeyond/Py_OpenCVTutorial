import cv2
import numpy as np

# define the shape enum
shape_Enum = {
    'rectangle': 0,
    'circle': 1,
    'pen': 2
}


# define the function in createTrackbar function
def nothing(x):
    pass


# define the mouse event function
def mouse_event(event, x, y, flags, param):
    global drawing, start, end, temp, shape, pen_size

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end = (x, y)
            if shape == shape_Enum['pen']:
                cv2.circle(img, (x, y), pen_size, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if shape == shape_Enum['rectangle']:
            cv2.rectangle(temp, start, (x, y), (b, g, r), size)
        elif shape == shape_Enum['circle']:
            cv2.circle(temp, (x, y), circleR, (b, g, r), size)
        elif shape == shape_Enum['pen']:
            cv2.circle(img, (x, y), pen_size, (b, g, r), -1)
        start = end = (0, 0)


if __name__ == "__main__":
    # define the variances
    drawing = False
    start, end = (-1, -1), (-1, -1)
    shape = shape_Enum['rectangle']

    # create the display board
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_event)
    temp = np.ones((512, 512, 3), np.uint8)*255

    # create track bar
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)
    cv2.createTrackbar('Size', 'image', 0, 10, nothing)      # size of pen
    cv2.createTrackbar('circleR', 'image', 4, 255, nothing)  # radius of circle
    cv2.createTrackbar('pen', 'image', 8, 15, nothing)

    # main loop
    while(True):
        # get the value of each track bar
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        size = cv2.getTrackbarPos('Size', 'image')
        circleR = cv2.getTrackbarPos('circleR', 'image')
        pen_size = cv2.getTrackbarPos('pen', 'image')

        # copy the previous temp to img and plot
        if shape == shape_Enum['pen']:
            img = temp
        else:
            img = np.copy(temp)
            if drawing and end != (0, 0):
                if shape == shape_Enum['rectangle']:
                    cv2.rectangle(img, start, end, (b, g, r), size)
                elif shape == shape_Enum['circle']:
                    cv2.circle(img, end, circleR, (b, g, r), size)

        cv2.imshow('image', img)
        if cv2.waitKey(50) == 27:
            break
        # convert the shape
        elif cv2.waitKey(50) == ord('r'):
            shape = shape_Enum['rectangle']
        elif cv2.waitKey(50) == ord('c'):
            shape = shape_Enum['circle']
        elif cv2.waitKey(50) == ord('p'):
            shape = shape_Enum['pen']
