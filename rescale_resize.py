import cv2 as cv

img=cv.imread("photos/sg11.png")
cv.imshow("image",img)
cv.waitKey(0)
#contruct a functiıon that rescale the actual image.

print(img.shape)
def resize(frame,scale):
    
    height= int(frame.shape[0]*scale) 
    print(height)
    width=int(frame.shape[1]*scale)
    dimentions=(width,height)
    
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA) 

cv.imshow("new_img",resize(img,0.1))
cv.waitKey(0)

