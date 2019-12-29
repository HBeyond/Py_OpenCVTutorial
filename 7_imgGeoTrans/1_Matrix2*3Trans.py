import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    lena = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/2_Python/p02_OpenCV_Tutorial/4_ImgBasicOperation/04_Imgs/1/lena.tiff"
    img_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/2_Python/p02_OpenCV_Tutorial/7_imgGeoTrans/1_imgs/drawing.jpg"

    img = cv2.imread(lena)
    img2 = cv2.imread(img_path)

    # 1. resize images
    # 1.1 resize the images as the fixed width and height
    height, width, channels = img.shape
    res = cv2.resize(img, (width*2, height*2))
    cv2.imshow('shrink', res)
    # 1.2 resize the images as the times of original x and y
    res2 = cv2.resize(img, None, fx=1, fy=2, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('zoom', res2)

    # 2. flip the images
    flip1 = cv2.flip(img, -1)
    flip2 = cv2.flip(img, 0)
    flip3 = cv2.flip(img, 1)
    titles = ['original', 'both x and y', 'x', 'y']
    images = [img, flip1, flip2, flip3]
    # for i in range(4):
    #     plt.subplot(2, 2, i+1)
    #     plt.imshow(images[i])
    #     plt.title(titles[i])
    #     plt.xlabel([]), plt.ylabel([])
    #     plt.show()
    for i in range(4):
        cv2.imshow(titles[i], images[i])

    # 3. translation the images
    rows, cols = img2.shape[:2]
    # define the translation matrix with the float32 type in numpy
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    # translation through affine transformation
    dst = cv2.warpAffine(img2, M, (cols, rows))
    cv2.imshow('shift', dst)

    # 4. rotation the images
    M2 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
    dst2 = cv2.warpAffine(img2, M2, (cols, rows))
    cv2.imshow('rotation', dst2)

    # 5. affine transformation
    pts1 = np.float32([[50, 65], [150, 65], [210, 210]])
    pts2 = np.float32([[50, 100], [150, 65], [100, 250]])
    # generate the transformation matrix
    M3 = cv2.getAffineTransform(pts1, pts2)
    dst3 = cv2.warpAffine(img2, M3, (cols, rows))
    cv2.imshow('affine transformation', dst3)


    cv2.waitKey(0)
