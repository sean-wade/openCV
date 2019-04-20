# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:34:59 2019

@author: Sean
"""

import cv2

img = cv2.imread('DLAM.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

thresh, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    #求轮廓的矩
    M = cv2.moments(cnt)
    print('轮廓的矩：', M)
    print('------------------------------------')
    print('轮廓的面积', int(M['m00']))
    print('#####################################')
    print('#####################################')
    print('#####################################')
    #计算质心
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(img, (cx, cy), 3, (0,0,255), -1)
    cv2.drawContours(img, cnt, -1, (0,0,255), 2)




cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()