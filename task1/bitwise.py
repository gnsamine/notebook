import cv2 as cv
import numpy as np 


blank=np.zeros((500,500), dtype="uint8")

rectangle= cv.rectangle(blank.copy(),(50,50),(450,450),255,-1)
circle= cv.circle(blank.copy(), (250,250),250,255,-1)


cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)


#and

andd=cv.bitwise_and(rectangle,circle)
cv.imshow("and",andd)

#or
orr=cv.bitwise_or(rectangle,circle)
cv.imshow("or",orr)


#xor
xorr=cv.bitwise_xor(rectangle,circle)
cv.imshow("xor",xorr)


#not

notr=cv.bitwise_not(rectangle)
cv.imshow("recnott", notr)



notc=cv.bitwise_not(circle)
cv.imshow("notc", notc)

cv.waitKey(0)
cv.destroyAllWindows()






