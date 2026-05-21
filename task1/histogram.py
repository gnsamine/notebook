import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 


img=cv.imread("photos/bardak.jpeg")

"""
images: list of images as numpy arrays. All images must be of the same dtype and same size.
channels: list of the channels used to calculate the histograms.
mask: optional mask (8 bit array) of the same size as the input image.
histSize: histogram sizes in each dimension
ranges: Array of the dims arrays of the histogram bin boundaries in each dimension
hist: Output histogram
accumulate: accumulation flag, enables to compute a single histogram from several sets of arrays.

"""


gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
histgray=cv.calcHist( [gray], [0], None, [256],[0,256] )

blank=np.zeros(img.shape[:2],dtype= "uint8")
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 300, [256,256,256] ,-1 )

masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow("mask",masked)
colors=("b","g","r")


plt.figure(1)
plt.xlim([0,256])
plt.figure(1)
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for i, col in enumerate(colors):
    hist=cv.calcHist(img, [i], None, [256], [0,256])
    plt.plot(hist,color=col, label=col)
    print(col)


plt.legend()
plt.show()





"""
#gray histogram

circle=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100, [256,256,256] ,-1 )
mask=cv.bitwise_and(gray,gray,mask=circle)


cv.imshow("mask",mask)

plt.figure(1)
plt.title("gray histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(histgray)
plt.xlim([0,256])
plt.show()

"""





cv.waitKey(0)
cv.destroyAllWindows()