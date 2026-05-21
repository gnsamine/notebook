import cv2 as cv


img= cv.imread("photos/katness.jpg")

cv.imshow("img",img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
 
haar_cascade = cv.CascadeClassifier("haarcascade.xml")
face= haar_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=10)

print(len(face))
print(face)

for x,y,w,h in face:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,256,256), 3)

cv.imshow("rectangled", img)

cv.waitKey(0)
cv.destroyAllWindows()