import cv2
import numpy as np

# if __name__ == "__main__":

drawing = False    # 是否开始画图
mode = True        # True：画矩形，False：画圆
start = (-1, -1)


def mouse_evernt(event, x, y, flags, param):
    global start, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode:
                cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
            else:
                cv2.circle(img, (x, y), 20, (0, 0, 255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), 20, (0, 0, 255), 1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_evernt)

while(True):
    cv2.imshow('image', img)

    if cv2.waitKey(50) == ord('m'):
        mode = not mode
    elif cv2.waitKey(50) == 27:
        break