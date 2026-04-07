import cv2 as cv


"""
Part 1 — ROI Tracking
Open your video (movie1.mp4)
Define a fixed ROI (e.g., center rectangle)
Draw a rectangle around it on each frame
👉 Expected:
Rectangle updates smoothly frame by frame
"""

"""
vid = cv.VideoCapture(0)
istrue,frame = vid.read()
h,w,l=frame.shape
print(h,w,l)
x = w // 2
y = h // 2

x1 = x - 300
y1 = y - 300
x2 = x + 300
y2 = y + 300


while True:
    ret, frame = vid.read()
    frame[y1:y2,x1:x2,2]=0
    #cv.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 20)
    cv.imshow("frame", frame)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()
"""
"""
Now make the ROI move horizontally across the video:
Start from left
Move right each frame
Reset when it reaches the edge
👉 This tests:
Your understanding of indexing

"""
"""
import cv2 as cv

vid=cv.VideoCapture(0)
istrue, frame= vid.read()
h,w,l=frame.shape
print(h,w,l)
x=h//2
y=w//2

x1=x-200
x2=x+200
y1=y-200
y2=y+200


while True:
    istrue, frame= vid.read()
    frame[x1:x2,y1:y2,2]=0
    frame[x1:x2,y1:y2,1]=0
    y1=y1+1
    y2=y2+1
    if y2==w:
        y2=y1
        y1=0
    cv.imshow("frame", frame)
    if cv.waitKey(2) & 0xFF==ord("a"):
        break

vid.release()
cv.destroyAllWindows()
"""
"""
Part 5 — Copy-Paste Trick (Fun)
Take ROI from one location
Paste it somewhere else in the same frame
👉 Example idea:
Copy center → paste top-left

"""

import cv2 as cv

vid=cv.VideoCapture(0)
tf,frame=vid.read()
h,w,_=frame.shape
print(h,w)

x=h//2
y=w//2

x1=x-200
x2=x+200
y1=y-200
y2=y+200

while True:
    istrue,frame=vid.read()
    copy=frame[x1:x2,y1:y2,:]
    frame[:(x2-x1),:(y2-y1),:]=copy
    
    
    cv.imshow("ka",frame)
    if cv.waitKey(20) & 0xFF==ord("d"):
        break


vid.release()
cv.destroyAllWindows()
        












