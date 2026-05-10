import cv2 as cv
import numpy as np

blank = np.zeros((900, 1500, 3), dtype="uint8")

drawing = False
color = (0, 200, 255) 
brush_size = 8


def draw(event, x, y, flags, param):
    global drawing, color

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == (cv.EVENT_MOUSEMOVE&cv.EVENT_LBUTTONDOWN):
        if drawing:
            cv.circle(blank, (x, y), brush_size, color, -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(blank, (x, y), brush_size, color, -1)


cv.namedWindow("Paint")
cv.setMouseCallback("Paint", draw)

while True:
    cv.imshow("Paint", blank)

    key = cv.waitKey(1) & 0xFF

    # Quit
    if key == ord('q'):
        break

cv.destroyAllWindows()