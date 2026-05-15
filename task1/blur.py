import cv2 as cv


img=cv.imread("photos/puma.png")

#average
average =cv.blur(img, (7,7))
cv. imshow ("Average Blur", average)
# Gaussian Blur

gauss = cv.GaussianBlur (img, (7,7), 3)
cv. imshow( "Gaussian Blur", gauss)


median= cv.medianBlur(img,7)
cv. imshow( "median", median)


bileteral =cv.bilateralFilter(img,45,155,65)
cv. imshow( "bileteral", bileteral)

cv.waitKey(0)
cv.destroyAllWindows()


