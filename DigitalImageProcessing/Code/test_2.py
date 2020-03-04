# Created by LiuMinXuan 2020/3/2 21:18 
# --coding:utf-8--
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width:%s, height:%s, channels:%s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for chn in range(channels):
                pv = image[row, col, chn]
                image[row, col, chn] = 255 - pv
    cv.imshow("show", image)


def create_inage():
    img = np.zeros([400, 400, 3], np.uint8)
    cv.imshow("new image", img)


src = cv.imread("../Images/6780100.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
t1 = cv.getTickCount()
access_pixels(src)
create_inage()
t2 = cv.getTickCount()
print("time %s" % ((t2 - t1)/cv.getTickFrequency()))
cv.waitKey(0)
cv.destroyAllWindows()
