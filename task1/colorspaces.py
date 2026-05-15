
import cv2 as cv
import matplotlib.pyplot as plt



img= cv.imread("photos/sg11.png")
cv.imshow("img", img)

img2= plt.imread("photos/sg11.png")
#plt.imshow(img)
#plt.show()

cv.imshow("img", img2)




#BGR to Gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#BGR to HSV
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

#BGR to LAB

lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)






cv.waitKey(0)
cv.destroyAllWindows()


