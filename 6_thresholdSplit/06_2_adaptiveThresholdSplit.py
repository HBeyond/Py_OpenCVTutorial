import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sudoku = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/6_thresholdSplit/1_Imgs/1/sudoku.jpg"

    img = cv2.imread(sudoku, cv2.CV_8UC1)

    # 1. fixed threshold value
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # 2. adaptive threshold
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
    th3 = cv2.adaptiveThreshold(img, 127, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
    th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)
    th5 = cv2.adaptiveThreshold(img, 127, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)
    titles = ['Original', 'Global(v=127)', 'Adaptive Mean', 'Adaptive Mean 2', 'Adaptive Gaussian', 'Adaptive Gaussian 2']
    images = [img, th1, th2, th3, th4, th5]

    for i in range(6):
        plt.subplot(3, 2, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i], fontsize=8)
        plt.xticks([]), plt.yticks([])

    plt.show()