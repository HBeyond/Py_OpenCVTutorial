import cv2
import numpy as np

if __name__ == "__main__":
    img_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/04_TestImg/1/lena.tiff"

    img = cv2.imread(img_path)

    # 1. get the pixel value at img[row, col], row = y, col = x
    pixel = img[100, 100]
    print(pixel)

    # 2.1 get the pixel blue channel value at at img[row, col], row = y, col = x
    pixel_blue = img[100, 100, 0]  # BGR[3], BGR[0] = B, BGR[1] = G, BGR[2] = R
    pixel_blue_high_performance = img.item(100, 100, 0)
    print(pixel_blue)
    print(pixel_blue_high_performance)

    # 3. change the pixel value
    # 3.1 change 3 channels at the same time
    img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    # 3.2 change 1 but higher efficient
    img.itemset((100, 100, 0), 19)
    print(img[100, 100])

    # 4. image attributes
    # 4.1 shape
    print(img.shape)  # output: rows(y), cols(x), channels, if image is gray, channels will not be output
    height, width, channels = img.shape
    print("height = ", height, ", width = ", width, ", channels = ", channels)
    # 4.2 data type
    print(img.dtype)
    # 4.3 total pixels of image
    print(img.size)  # rows * cols * channels

    # 5. ROI
    roi = img[200:400, 200:400]
    cv2.imshow("ROI", roi)

    # 6. channels split and merge
    # 6.1 usual method = ineffective method
    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))
    # 6.2 numpy index method = high efficient method
    b = img[:, :, 0]
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)

    # 7. exercise
    hat = img[100:300, 200:400]
    hat_r = hat[:, :, 2]
    cv2.imshow('hat_r', hat_r)

    cv2.waitKey(0)

