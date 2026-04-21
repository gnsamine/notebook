
"""
Task 5: Region Highlighting
Detect edges
Dilate them
Overlay the edges on the original image (colored, e.g. red)
👉 Youll need to:
Convert grayscale → BGR
Use masking or blending
"""

import cv2 as cv


img= cv.imread("task1/photos/bardak.jpeg")
cv.imshow("img", img)

gry= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
dilated= cv.dilate(gry,(3,3), iterations=3)

cv.imshow("gry", gry)


cv.waitKey(0)
cv.destroyAllWindows()















"""
Task 6: Custom Filter
Recreate blur manually using NumPy:
Don’t use cv.blur
Use averaging over kernel window
👉 This builds real understanding of convolution
"""


