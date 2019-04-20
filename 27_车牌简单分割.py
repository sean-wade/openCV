# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:45:34 2019

@author: Sean
"""

import cv2

#车牌分割的简单方法，无法准确提取汉字
img = cv2.imread('cp2.jpg')
blur = cv2.medianBlur(img,5)  #中值滤波
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

i = 0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    if w>15 and h>20 and w<100 and h<100:
        i += 1
        ROI = thresh[y:y+h,x:x+w]
        ROI = cv2.bitwise_not(ROI)
        cv2.imwrite('cp/%d.bmp'%i, ROI)
        cv2.rectangle(img, (x,y),(x+w, y+h),(0,0,0),4)
#cv2.drawContours(img, contours, -1, (0,255,255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()