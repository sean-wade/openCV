# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:07:15 2019

@author: Sean
"""

import cv2

img = cv2.imread('yuan.bmp')
temp = img.copy()

gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)
thresh, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
#    cv2.drawContours(img, cnt, -1, (0,255,0), 2)
    hull = cv2.convexHull(cnt)  #默认returnPoints = True
    print(len(hull))
    for i in range(0,len(hull)):
        print(hull[i][0][0],hull[i][0][1])
        ptHull = (hull[i][0][0],hull[i][0][1])
        if i < len(hull) - 1:
            ptHull2 = (hull[i+1][0][0],hull[i+1][0][1])
        else:
            ptHull2 = (hull[0][0][0],hull[0][0][1])
        cv2.line(img,ptHull,ptHull2,(0,0,255),2,cv2.LINE_AA)
        cv2.circle(img,ptHull,3,(0,255,0),2,cv2.LINE_AA)
        
cv2.imshow('Hull',img)
cv2.waitKey(0)
cv2.destroyAllWindows()