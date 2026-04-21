import cv2 as cv

img= cv.imread("task1/photos/puma.png")
cv.imshow("puma", img)
print(img.shape)



#convert the img to graysclae (intensity distributions of the image not the color)
grayimg= cv.cvtColor(img, cv.COLOR_BGR2GRAY,cv.BORDER_CONSTANT,(0,0),0)
cv.imshow("pumagray", grayimg)

"""
The kernels will define the size of the convolution, the weights applied to it,
and an anchor point usually positioned at the center.

"""
#blur the image
blur=cv.blur(img,(17,17), cv.BORDER_CONSTANT,(0,0),0 )
cv.imshow("blur", blur)
print(blur.shape)


#find edges
edge= cv.Canny(grayimg,75,75)

#cv.imshow("edge", edge)
#dilate 
dilated=cv.dilate(edge,(-17,-17), iterations=3)
#cv.imshow("dilated", dilated)

#erote the image
eroted= cv.erode(dilated,(3,3), iterations=2)
#cv.imshow("eroded", eroted)
#cv.imwrite('edges.jpg', eroted)

#resize
resized= cv.resize(img, (400,400), cv.INTER_AREA)
cv.imshow("resized", resized)

#crop 
cropped= img[:  (img.shape[1]//2), (img.shape[1]//2):]
#cv.imshow("cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()

"""


"""