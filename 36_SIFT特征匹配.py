# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:37:22 2019

@author: Sean
"""
# =============================================================================
# SIFT特征匹配算法，可用于全景图拼接
# =============================================================================
import cv2
import numpy as np

img = cv2.imread('wd.jpg')
img2= cv2.imread('wd2.jpg')

gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

bf = cv2.BFMatcher()

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x:x.distance)

result = np.zeros((img.shape[1] + img2.shape[1], img.shape[0]),np.uint8)

result = cv2.drawMatches(img, kp1, img2, kp2, matches[:30], result, (0,255,0),flags = 0)




cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()