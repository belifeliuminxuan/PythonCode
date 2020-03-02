# Created by LiuMinXuan 2020/3/2 19:40
# --coding:utf-8--
import cv2 as cv
import numpy as np


# 获取摄像头采集
def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


# 获取图片信息
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("../Images/6780100.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
get_image_info(src)
# 将图像转换为灰色图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("./result.png", gray)
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
