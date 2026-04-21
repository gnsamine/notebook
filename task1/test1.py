"""
Write a script where:
Pressing keys does actions:
g → grayscale
b → blur
e → edge detection
r → reset image
👉 Hint: use cv.waitKey() properly
👉 This is your first interactive program

"""
import cv2 as cv

img=cv.imread("task1/photos/puma.png")

inp=img
#name="img"
while True:
    
    cv.imshow("output", inp)
    pasw = (cv.waitKey(0) & 0xFF)

    if pasw == ord("q"):
        break
    elif pasw == ord("g"):
        grey= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        #name="gray"
        inp=grey
        print("i")
    elif pasw == ord("b"):
        blur=cv.blur(img,(7,7), cv.BORDER_DEFAULT)
        #name = "blur"
        inp = blur
        print("j")
    elif pasw ==  ord("e"):
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        edge= cv.Canny(gray,75,75)
        #name="edge"
        inp=edge
        print("k")
    elif pasw == ord("r"):
       inp= img
       #name= "img"    
cv.destroyAllWindows()

