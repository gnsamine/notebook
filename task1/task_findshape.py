"""
Create an image containing:
circles
triangles
rectangles
overlapping shapes
Your program must:
detect contours
classify each shape
compute contour area
compute perimeter
label shapes on image
Required concepts:
grayscale
blur
threshold OR canny
contours
contour approximation

"""

import cv2 as cv
import numpy as np



blank =np.zeros((1024,2048,3), dtype="uint8")

cv.imshow("blank", blank)
cv.rectangle(blank,(blank.shape[1]//2-200,blank.shape[0]//2-200),(blank.shape[1]//2+200,blank.shape[0]//2+200), (0,200,255),-1)
cv.rectangle(blank,(blank.shape[1]//2+200,blank.shape[0]//2+300),(blank.shape[1]//2+800,blank.shape[0]//2+400), (200,0,255),-1)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 160, (0,20,250), -1)

triangle_cnt = np.array([(315,400), (600,700), (450,900)])
triangle_cnt2= np.array([(300,400), (200,400), (200,50),])
triangle_cnt3=np.array([(blank.shape[1]//2+400,blank.shape[0]//2),(blank.shape[1]//2+800,blank.shape[0]//2), (blank.shape[1]//2+600,blank.shape[0]//2-400)])

tri =cv.drawContours(blank, [triangle_cnt,triangle_cnt2,triangle_cnt3], -1, (0,255,0),-1)
cv.imshow("circle",tri)

gray=cv.cvtColor(tri,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)

edge=cv.Canny(gray,50,150)


_,thres=cv.threshold(edge,100,255,cv.THRESH_BINARY,)
cv.imshow("th", thres)
blank2 =np.zeros((1024,2048,3), dtype="uint8")

contours, hierarchies = cv. findContours (thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
draw= cv.drawContours(blank2,contours,-1,(0,200,200))
cv.imshow("draw",draw)

approx = cv.approxPolyDP()





cv.waitKey(0)
cv.destroyAllWindows()







