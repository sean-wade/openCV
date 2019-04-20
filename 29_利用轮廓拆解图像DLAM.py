# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:22:39 2019

@author: Sean
"""
#拆解哆啦A梦

import cv2
import numpy as np

img = cv2.imread('DLAM.jpg')
temp = img.copy()

black1 = np.zeros(img.shape, np.uint8)
black2 = np.zeros(img.shape, np.uint8)
white = np.ones(img.shape, np.uint8)*255

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(contours))

while True:
    for i in range(len(contours)):
        
        black1 = black2.copy()
        img = temp.copy()
        cv2.drawContours(black1, contours, i, (255,255,255), -1)
        cv2.drawContours(img, contours[i], -1, (0,0,255), 3)
        mask1 = cv2.cvtColor(black1, cv2.COLOR_BGR2GRAY)
        result = cv2.bitwise_and(temp, temp, mask = mask1)
        cv2.imshow('result',result)
        cv2.imshow('src', img)
        cv2.imshow('black', black1)
        
        if cv2.waitKey(0)==27:
            break
    break

#cv2.drawContours(temp, contours, -1, (0,0,255), -1)
#cv2.imshow('t',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()






