import cv2
import numpy as np

if __name__ == "__main__":

    # 1. open camera
    cap = cv2.VideoCapture(0)

    # 2. set the threshold of blue
    lower_blue = np.array([100, 110, 110])
    upper_blue = np.array([130, 255, 255])
    # 2.1 set the threshold of green
    lower_g = np.array([40, 90, 90])
    upper_g = np.array([70, 255, 255])
    # 2.2 set the threshold of red
    lower_r = np.array([160, 120, 120])
    upper_r = np.array([179, 255, 255])


    # 3. track begin
    while(True):
        # 4. capture one frame
        ret, frame = cap.read()

        # 5. convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 6. check
        mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_g = cv2.inRange(hsv, lower_g, upper_g)
        mask_r = cv2.inRange(hsv, lower_r, upper_r)
        mask = mask_b + mask_g + mask_r

        # 7. only save the part in blue
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(1) == ord('q'):
            break