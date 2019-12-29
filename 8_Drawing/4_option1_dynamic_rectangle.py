import cv2
import numpy as np

drawing = False    # 是否开始画图
start, end = (-1, -1), (-1, -1)


def mouse_event(event, x, y, flags, param):
    global drawing, start, end, temp

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # black_img = np.zeros((512, 512, 3), np.uint8)
            # cv2.bitwise_and(img, black_img, dst=img)
            # cv2.rectangle(img, start, (x, y), (0, 0, 255), 1)
            end = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(temp, start, (x, y), (0, 0, 255), 1)
        start = end = (0, 0)


cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)
temp = np.zeros((512, 512, 3), np.uint8)
# img = np.zeros((512, 512, 3), np.uint8)

while(True):
    img = np.copy(temp)
    if(drawing and end != (0, 0)):
        cv2.rectangle(img, start, end, (255, 0, 0), 2)

    cv2.imshow('image', img)
    if cv2.waitKey(50) == 27:
        break