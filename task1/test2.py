
"""
Task 5: Region Highlighting
Detect edges
Dilate them
Overlay the edges on the original image (colored, e.g. red)
👉 Youll need to:
Convert grayscale → BGR
Use masking or blending
"""

import cv2 as cv


img= cv.imread("task1/photos/library.jpeg")
cv.imshow("img", img)
blur=cv.GaussianBlur(img,(5,5),2)
cv.imshow("new", img)

gry= cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
edge=cv.Canny(gry,45,45)

dilated= cv.dilate(edge,(17,17), iterations=4)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if dilated[i,j]!=0:
            img[i,j,0]=250
            img[i,j,1]=0
            img[i,j,2]=250

    
cv.imshow("new", img)

cv.waitKey(0)
cv.destroyAllWindows()




