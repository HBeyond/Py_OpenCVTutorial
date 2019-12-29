import os
import cv2
import numpy as np

path = '/home/beyoung/VisionStudy/camNormal/'
filelist = os.listdir(path)

fps = 5 #视频每秒n帧
size = (1280, 720) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("/home/beyoung/Desktop/outputVideo.avi", cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
#视频保存在当前目录下

# for item in filelist:
#     if item.endswith('.jpg'):
#     #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
#         item = path + item
#         img = cv2.imread(item)
#         video.write(img)

# sort the image names by name
filename_vec = []
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith('.jpg'):
            filename_vec.append(int(filename[:-4]))
filename_vec.sort()

# write the images into a video
for i in range(len(filename_vec)):
    img_path = path + str(filename_vec[i]) + '.jpg'
    img = cv2.imread(img_path)
    video.write(img)

video.release()
cv2.destroyAllWindows()