import cv2

if __name__ == "__main__":
    image_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/02_1_TestImgs/"

    img = cv2.imread(image_path + "lena512color.tiff", cv2.IMREAD_UNCHANGED)

    cv2.namedWindow("lena", cv2.WINDOW_NORMAL)

    cv2.imshow("lena", img)

    key = cv2.waitKey(0)

    if key == 13:

        cv2.imwrite(image_path + "lena512color_bmp.bmp", img)

        cv2.imwrite(image_path + "lena512color_jpg95.jpg", img)

        cv2.imwrite(image_path + "lena512color_jpg20.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 20])

        cv2.imwrite(image_path + "lena512color_png.png", img)

        cv2.imwrite(image_path + "lena512color_png9.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

