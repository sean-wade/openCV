# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:35:10 2019

@author: Sean
"""

import cv2
import numpy as np

#旋转校正
img = cv2.imread('ewm.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret,thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

k1 = np.ones((7,7), np.uint8)
thresh = cv2.dilate(thresh, k1, iterations = 1)
thresh = cv2.erode(thresh, k1, iterations = 1)

cv2.imshow('thresh',thresh)
thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img, contours, 5, (0,0,255))

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)

cv2.drawContours(img, [box], 0, (0,0,255), 2)

#angle = rect[2]
#print(abs(rect[2]))
if abs(rect[2]) <45:
    angle = rect[2]
if abs(rect[2])>45 and abs(rect[2])<90:
    angle = 90 - abs(rect[2])
#print(angle)
center = tuple(rect[0])

matrix = cv2.getRotationMatrix2D(center, angle, 1)
img1 = cv2.warpAffine(img, matrix, (img.shape[1],img.shape[0]))


cv2.imshow('src',img)
cv2.imshow('rotate',img1)

cv2.imwrite('ewmRotate.jpg',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
