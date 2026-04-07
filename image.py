"""
Aim:

Access pixel values and modify them
Access image properties
Set a Region of Interest (ROI)
Split and merge images

"""

import cv2 as cv
img = cv.imread("photos/sg2.png")
print( img.shape )

cv.imshow("win",img)
cv.waitKey(0)


#access the certain part of the picture
# img[:(row),:(column),:(channel)] if ypu set channel to 0=white-black  
"""
blue_channel = img[900:950,1500:1550, :] 
cv.imshow("win2",blue_channel)
cv.waitKey(0)

#take some pixels and see the 
new_img=img[400:950,1500:1950, :]
new_img[100:130,200:400,:]=0

cv.imshow("win3",new_img)
cv.waitKey(0)
"""
"""
#see the properties (row, column, channel)
print(img[:,:,0].shape)

#see all pixels
new_img=img[400:950,1500:1950, :]
dimen=new_img.shape
print("dimentions:", dimen)

print(new_img.size)

print(dimen[0]*dimen[1]*dimen[2]==new_img.size)


"""

video=cv.VideoCapture("videos/movie1.mp4")

while True:
    isTrue, frame = video.read()
    #print(isTrue)
    #print(frame)
    #cv.imshow('Video', frame[400:600])
    #this slicing cuts the pixels in one frame
    cv.imshow('Video', frame)

    if cv.waitKey(5) & 0xFF==ord('a'):
        print(a,type(a))
# waitKey: determines the speed, it waits ..ms after grab the frame. for do not wait, use cv.pollKey()
#Pause the video for 5 milliseconds. During this pause, 
#check if the user has pressed the 'd' key on their keyboard. If they have, stop the loop and close the video immediately.
        break


      
video. release()
cv. destroyAllWindows ()



