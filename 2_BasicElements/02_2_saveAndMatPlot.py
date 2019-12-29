import cv2
import matplotlib.pyplot as mp

if __name__ == "__main__":
    img_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/02_2_TestImgs/"

    img_grey_cv = cv2.imread(img_path+"lena.jpg", cv2.IMREAD_GRAYSCALE)

    # cv show grayscale
    cv2.imshow("lena", img_grey_cv)
    cv2.waitKey(1000)  # show 1000 ms

    # matplot show
    mp.imshow(img_grey_cv, cmap = 'gray')
    # mp.show()

    img_color = cv2.imread(img_path+"lena.jpg")

    # cv show, cv channel is BGR
    cv2.imshow("lena2", img_color)

    # matplot show, matlab channel is RGB
    img_color_RGB = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

    mp.figure(2)
    mp.subplot(121), mp.imshow(img_color)

    mp.subplot(122)
    mp.xticks([]), mp.yticks([])  # 隐藏x和y轴
    mp.imshow(img_color_RGB)
    mp.savefig(img_path+"matplotSave.jpg")
    mp.show()

