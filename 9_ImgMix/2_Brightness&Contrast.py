import cv2
import numpy as np

if __name__ == "__main__":
    lena_path = '/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/9_ImgMix/Imgs/1/lena.jpg'
    img = cv2.imread(lena_path)

    res = np.uint8(np.clip((1.5*img + 10), 0, 255))
    tmp = np.hstack((img, res))

    cv2.imshow('image', tmp)
    cv2.waitKey(0)