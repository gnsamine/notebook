import cv2 as cv
import numpy as np

"""
What is an edge? A sharp change in brightness
Ideal edge is a step function in certain direction.
"""

img= cv.imread("photos/whitestripes.webp")
cv.imshow("original", img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)


blur=cv.blur(gray, (5,5))
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125,75)
cv.imshow("canny", canny)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
_,threshold= cv.threshold(canny,145,255,cv.THRESH_BINARY)
cv.imshow("thresholdi", threshold)

blank2=np.zeros((img.shape),  dtype="uint8")
cv.imshow("blank2",blank2)
draw= cv.drawContours(blank2, contours,-1, (0,100,200), thickness=2)
cv.imshow("drawcontours", draw)








blank=np.zeros((900,1500,3), "uint8")
rec=cv.rectangle(blank,(100,500),(250,250),(0,126,0),thickness=8)
recCirc=cv.circle(rec,(blank.shape[1]//2,blank.shape[0]//2), 400,(0,200,0), thickness=6)
cv.imshow("blank",recCirc)

gray2=cv.cvtColor(recCirc,cv.COLOR_BGR2GRAY)
canny2=cv.Canny(gray2,0,125)
cv.imshow("canny", canny2)


_, thresh = cv.threshold(gray2, 100, 300, cv.THRESH_BINARY)
cv.imshow("threshold", thresh)

"""threshold and canny are different"""
contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(len(contours))
print(hierarchies)


"""
. RETR_LIST
This is the simplest of the four flags (from explanation point of view).
It simply retrieves all the contours, but doesn't create any parent-child relationship.
Parents and kids are equal under this rule, and they are just contours. 
ie they all belongs to same hierarchy level.
"""




cv.waitKey(0)
cv.destroyAllWindows()

