"""we can use an Affine Transformation to express:
Rotations (linear transformation)
Translations (vector addition)
Scale operations (linear transformation)
"""



"""translation, define translation function"""

import cv2 as cv
import numpy as np 


def translate (img, x, y) :
    transMat = np.float32([[1,0, x], [0, 1, y]])
    print(transMat)
    dimensions = (img.shape[1]*2, img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

img=cv.imread("photos/puma.png")
(height, width) = img.shape[:2]

print("tuple:",(height, width))
height= img.shape[0]
width = img.shape[1] 
print("rows:", height)
print("columns:", width)


translated= translate(img,-300,100)
cv.imshow("translated", translated)


"""rotation"""

def rotation(img, angle,rotPoint=None):
    height, width = img.shape[0], img.shape[1]
    #here we use numpy
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv. getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    #opencv uses (width, height) here we use opencv
    return cv. warpAffine(img, rotMat, dimensions)

rotated= rotation(img,30)
cv.imshow("rotated",rotated)


"""resize"""
resized = cv.resize(img, (50,50), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resized)

"""filp"""
flipped= cv.flip(img,-1)
cv.imshow("flipped", flipped)

"""crop"""
cropped= img[:300,400:800]
cv.imshow("cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()