# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:19:39 2019

@author: Sean
"""

import cv2

img = cv2.imread('star3.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('g',gray)

#2:blocksize(邻域大小)， 3：ksize(sobel算子孔径大小)，0.04：Harris检测常量参数(通常默认取值0.04~0.06)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

ret, thresh = cv2.threshold(dst, 0.01, 255, cv2.THRESH_BINARY)

cv2.imshow('thr', thresh)

img[dst>0.01] = [0,255,0]

for i in range(0, img.shape[0]): 
    for j in range(0, img.shape[1]):
        if(dst[i, j] > 0.01):
            cv2.circle(img, (j,i), 5, (255,0,255), 2, cv2.LINE_AA)

cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()