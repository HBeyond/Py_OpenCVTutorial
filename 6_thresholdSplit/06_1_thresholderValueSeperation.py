import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    gradient_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/06/1/gradient.jpg"

    img = cv2.imread(gradient_path)

    # threshold split
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    ret, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_MASK)
    # ret, th7 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
    # ret, th8 = cv2.threshold(img, 127, 255, cv2.THRESH_TRIANGLE)

    titles = ['original', 'binary', 'binary_inv', 'trunc', 'toZ', 'toz_inv', 'mask']
    images = [img, th1, th2, th3, th4, th5, th6]

    for i in range(7):
        plt.subplot(2,4,i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], fontsize=8)
        plt.xticks([]), plt.yticks([])

    plt.show()