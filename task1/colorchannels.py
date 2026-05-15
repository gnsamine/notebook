import cv2 as cv
import numpy as np

#splitmerge.py - OpenCV - Visual Studio Code
img = cv. imread ('Photos/sg2.png')
cv.imshow( "img", img)
b, g,r = cv.split(img)


cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow ("Red", r)


blank = np.zeros(img.shape[:2], dtype= "uint8")

blue = cv. merge ([b, blank, blank])
green = cv. merge ([blank, g, blank])
red = cv. merge ([blank,blank, r])


cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow ("Red", red)


print (img. shape)
print (b. shape)
print (g. shape)
print (r. shape)
cv. waitKey (0)