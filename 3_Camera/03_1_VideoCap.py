import cv2

if __name__ == "__main__":

    video_save_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/p02_OpenCV_Tutorial/03_1_VideoSavePath/"

    capture = cv2.VideoCapture(0)  # open the camera on computer

    width, height = capture.get(3), capture.get(4)

    print(width, height)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # set save code mode and create VedieWriter instance
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    outfile = cv2.VideoWriter(video_save_path + 'record.mp4', fourcc, 25., (640,480))

    while(capture.isOpened()):

        ret, frame = capture.read()

        if ret == True:

            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            gray = frame

            outfile.write(gray)

            cv2.imshow("frame", gray)

            if cv2.waitKey(1) == ord('q'):

                break