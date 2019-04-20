# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:44:10 2019

@author: Sean
"""

import cv2
import numpy as np

img = cv2.imread('star.bmp')
temp = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 250, cv2.THRESH_BINARY_INV)
thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(len(contours))
cv2.drawContours(img, contours, -1, (0,0,255), 2)

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
#    print(rect)
    cv2.putText(img, 'width = %0.2f, height = %0.2f'%(rect[1][0], rect[1][1]), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
    box = cv2.boxPoints(rect)    #输入旋转矩形，输出点集
#    print(box)
    box = np.int0(box)
#    print(box)
    img = cv2.drawContours(img, [box], 0, (0,255,0), 2)
#    cv2.circle(img, tuple(box[3]), 3, (255,0,0), 2)
    print('----------><---------')




cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()