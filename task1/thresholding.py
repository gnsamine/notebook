import cv2 as cv


img= cv.imread("photos/puma.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, thresh= cv.threshold(gray,140 ,255, cv.THRESH_BINARY)
cv.imshow("thresholded", thresh)

threshold, thresh_inv= cv.threshold(gray,140 ,255, cv.THRESH_BINARY_INV)
cv.imshow("thresholded inverted", thresh_inv)


tresh_adv= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 9, 3)
cv.imshow("adaptive thresholded", tresh_adv)


tresh_adv2=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,5)
cv.imshow("adaptive thresholded2", tresh_adv2)





cv.waitKey(0)
cv.destroyAllWindows()



