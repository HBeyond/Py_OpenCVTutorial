import cv2
import numpy as np
import matplotlib.pyplot as plt


def second_squares_generation():


def hour_squares_generation():


def static_clock_board_generation():
    # 1. generate seconds squares
    second_squares_generation()
    # 2. generate hour squares
    hour_squares_generation()


def dynamic_clock_board_generation():
    # 1. get the real time

    # 2.



if __name__ == "__main__":
    # 1. white background
    img_rows = 1024
    img_cols = 1024
    img_channels = 3
    img = np.ones((img_rows, img_cols, img_channels), np.uint8)*255

    # 2. clock board information
    circle_center_x = 512
    circle_center_y = 512
    circle_center = (circle_center_x, circle_center_y)
    circle_radius = 400
    circle_color = (0, 0, 0)
    circle_degree = 360
    hour_square_number = 12
    second_square_number = 60

    # 3. generate the clock board
    # 3.1 plot board
    cv2.circle(img, circle_center, circle_radius, circle_color)
    # 3.2 generate static clocks board
    static_clock_board_generation()
    # 3.3 generate dynamic clocks board
    dynamic_clock_board_generation()

    # 6. loop
    # while True:
    #     print(1)
    cv2.namedWindow('clock')
    cv2.imshow('clock', img)
    cv2.waitKey(0)