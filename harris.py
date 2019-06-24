import cv2
import numpy as np
filename = 'chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
window_size = 2
k = 0.04
dy, dx = np.gradient(gray)
Ixx = dx ** 2
Ixy = dy * dx
Iyy = dy **2
height = gray.shape[0]
width = gray.shape[1]
newImg = np.zeros(gray.shape)
offset = 1
for y in range(offset, height-offset):
        for x in range(offset, width-offset):
            #Calculate sum of squares
            Sxx =np.sum(Ixx[y-offset :y+offset+1, x-offset:x+offset+1])
            Sxy =np.sum (Ixy[y-offset:y+offset+1, x-offset:x+offset+1])
            Syy =np.sum (Iyy[y-offset:y+offset+1, x-offset:x+offset+1])
            #Find determinant and trace, use to get corner response
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = det - k*(trace**2)

            #If corner response is over threshold, color the point and add to corner list
            if (r >100000000) :
                 newImg[y,x] = 255
color_img = img.copy()
color_img[newImg>0] = [0,0,255]

cv2.imshow('dst',color_img)
cv2.imwrite('output.png', color_img)
