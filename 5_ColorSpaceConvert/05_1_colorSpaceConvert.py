import cv2

if __name__ == "__main__":
    img_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/04_TestImg/1/lena.tiff"
    img = cv2.imread(img_path)

    # 1. color space convert
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img_gray', img_gray)
    # 1.1 all the color mode
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print(flags)

    cv2.waitKey(0)