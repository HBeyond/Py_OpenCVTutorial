import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    # 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
    cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)

    # 画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # 画一个填充红色的圆，参数2：圆心坐标，参数3：半径 参数4线宽=-1代表填充
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    # 在图中心画一个填充的半椭圆
    # 参数2：椭圆中心(x,y)
    # 参数3：x/y轴的长度
    # 参数4：angle---椭圆的旋转角度
    # 参数5：startAngle---椭圆的起始角度
    # 参数6：endAngle---椭圆的结束角度, 180 represents half circle
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 270, (255, 0, 0), -1)

    # 画多边形
    # 定义四个顶点坐标
    pts = np.array([[10, 5], [50, 10], [70, 20], [20, 30]], np.int32)
    # 顶点个数：4，矩阵变成4*1*2维
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))

    # 添加文字
    # 参数2：要添加的文本
    # 参数3：文字的起始坐标（左下角为起点）
    # 参数4：字体
    # 参数5：文字大小（缩放比例）
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font,
                4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

    cv2.imshow('img', img)
    cv2.waitKey(0)