# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:36:42 2019

@author: Sean
"""

import cv2
import numpy as np


img = cv2.imread('star3.bmp')

temp = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)


img = cv2.drawKeypoints(img, kp, img, (0,255,0), \
                        flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Sift', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
