import cv2

if __name__ == "__main__":
    vedio_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/03_2_TestVedio/2018-04-21_T_09-03-50.187_GMT.mp4"

    capture = cv2.VideoCapture(vedio_path)

    print(capture.isOpened())

    while(capture.isOpened()):

        ret, frame = capture.read()

        # if ret == True:

        cv2.imshow('local_vedio', frame)

        if cv2.waitKey(29) == ord("q"):

            break