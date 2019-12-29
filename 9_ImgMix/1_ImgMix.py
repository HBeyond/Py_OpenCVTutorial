import cv2
import numpy as np

if __name__ == "__main__":
    lena_path = '/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/9_ImgMix/Imgs/1/lena.jpg'
    small_lena_path = '/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/9_ImgMix/Imgs/1/lena_small.jpg'
    openCV_path = '/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/9_ImgMix/Imgs/1/opencv-logo-white.png'

    # 1. images adding
    x = np.uint8([250])
    y = np.uint8([10])
    print(cv2.add(x, y))   # 250+10 = 260 => 255
    print(x+y)             # 250+10 = 260 % 256 = 4

    # 2. overlay two images
    img1 = cv2.imread(small_lena_path)
    img2 = cv2.imread(openCV_path)
    res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
    cv2.imshow('overlay', res)

    # 3. bitwise operation
    # create the roi
    img3 = cv2.imread(lena_path)
    rows, cols = img2.shape[:2]
    roi = img3[:rows, :cols]
    # create the mask
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # keep the background except the logo in img3, and operation replaces the part
    img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(img3_bg, img2)
    img3[:rows, :cols] = dst
    # show
    cv2.imshow('mask', mask)
    cv2.imshow('mask_inv', mask_inv)
    cv2.imshow('img3_bg', img3_bg)
    cv2.imshow('dst', dst)
    cv2.imshow('bitwise', img3)

    cv2.waitKey(0)