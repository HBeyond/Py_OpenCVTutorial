import cv2
import numpy as np


def mouse_pos(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


# if __name__ == "__main__":
img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('image')

cv2.setMouseCallback('image', mouse_pos)

while(True):
    cv2.imshow('image', img)

    if cv2.waitKey(20) == 27:
        break
