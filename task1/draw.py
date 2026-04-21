import cv2 as cv
import numpy as np


#access a photo

img= cv.imread("task1/photos/puma.png")
cv.imshow("photo", img)



#create blanck image
blank = np.zeros( (500,500,3), dtype="uint8" ) 
cv.imshow("blank", blank)


#paint the image to the certain color
blank[:,:]= 100,0,255
cv.imshow("colored", blank)

# paint some portion of image
blank[:300,:200]= 0,200,0
cv.imshow("coloredpartially", blank)
#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,0),thickness=5)
cv.imshow("rectangle", blank)


#fill the rectangle with a color
cv.rectangle(blank,(250,250),(400,350),(0,0,0),thickness=5)
cv.imshow("rectangle", blank)

#while drawing rectangle use the row/column
cv.rectangle(blank,(0,0),(blank.shape[0]//2, blank.shape[1]//2),(0,250,250),thickness=4)
cv.imshow("rectangle", blank)

#draw a circle / point
cv.circle(blank,(blank.shape[0]//2, blank.shape[1]//2),50,(0,0,0), thickness=-1)
cv.imshow("wcircle", blank)

#draw a line

cv.line(blank,(0,0),(blank.shape[0]//2, blank.shape[1]//2),(250,250,250), thickness=5)
cv.imshow("wline", blank)


#put text

blank2 = np.zeros((500,500,3), dtype="uint8")
cv.imshow("blank2", blank2)

cv.putText(blank2," world or word?",  (blank2.shape[0]//2-100,blank2.shape[1]//2), fontScale=1, fontFace=cv.FONT_HERSHEY_TRIPLEX ,color=(0, 250, 0 ) )
cv.imshow("blank2", blank2)

cv.waitKey(0)
cv.destroyAllWindows()
