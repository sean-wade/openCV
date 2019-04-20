# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:34:59 2019

@author: Sean
"""

import cv2
import numpy as np

img = cv2.imread('DLAM.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([88,43,46])
upper_blue = np.array([124,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

ret = cv2.bitwise_and(img, img, mask = mask)
        
cv2.imshow('mask', mask)
cv2.imshow('img', img)
cv2.imshow('ret', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()