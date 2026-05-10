"""
Task 10: Simple Paint App
Blank canvas
Click & drag to draw (mouse callback)
Press key to change color
👉 This introduces:
event handling
user interaction
"""

import numpy as np 
import cv2 as cv

xlist=[]
ylist=[]


def getxy(evt,x,y,flags,userdata):
    
    print("evt: ",str(evt))
    print("X,Y: ",str(x),str(y) )
    print("flags: ", str(flags))
    print("ud: ", userdata)
    if flags==8:
        xlist.append(x)
        ylist.append(y)
    


blank=np.zeros((900,1500,3), "uint8")
cv.imshow("blank", blank)
cv.setMouseCallback("blank", getxy)

cv.waitKey(0)

blank2=np.zeros((900,1500,3), "uint8")
"""xylist=[]
for indx, i in enumerate(xlist):

    for indy, j in enumerate(ylist):
        if indx == indy:
                xylist.append((i, j))
print(xylist)"""
xylist = list(zip(xlist, ylist))
    

for x,y in xylist:
    circ=cv.circle(blank2,(x,y),2,(0,255,100),-1)

    #blank2[k]=(0,200,200)

dilated=cv.dilate(circ,(5,5), iterations=13)

cv.imshow("blk",dilated)



cv.waitKey(0)

cv.destroyAllWindows()



