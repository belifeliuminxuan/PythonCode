import cv2 as cv
src = cv.imread("../Images/6780100.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)
cv.destroyAllWindows()
