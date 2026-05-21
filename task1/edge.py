import cv2 as cv
import numpy as np

img= cv.imread("photos/puma.png")
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow("gray", gray)


"""
A transition from black-to-white results in a positive slope.
A transition from white-to-black results in a negative slope.
(cv.CV_8U), it cannot hold negative numbers.
"""
lapacian= cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lapacian))
cv.imshow("lap", lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
cv.imshow ('Sobel X', sobelx)

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow ('Sobel Y', sobely)



combinedSobel= cv.bitwise_and(sobelx,sobely)
cv.imshow ('Sobel Combined', combinedSobel)


blur= cv.blur(gray, (3,3))
canny= cv.Canny(blur, 100,256)
cv.imshow("canny", canny)



cv.waitKey(0)
cv.destroyAllWindows()







