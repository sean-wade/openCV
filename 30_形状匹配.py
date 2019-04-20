# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:34:59 2019

@author: Sean
"""

import cv2

img = cv2.imread('num2.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

thresh, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours[0], -1, (0,0,255), 3)


for cnt in contours:
    #形状匹配
    ret = cv2.matchShapes(cnt, contours[0], cv2.CONTOURS_MATCH_I2, 0.0)
    print(ret)
    if ret<0.6:
        cv2.drawContours(img, cnt, -1, (0,255,255), 2)
        
cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()