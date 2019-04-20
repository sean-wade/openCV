# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:38:10 2019

@author: Sean
"""

import numpy as np
import cv2


img = cv2.imread('bird.jpg')
cv2.imshow('bird', img)


mask = None

seed_pt = (10, 10)#种子点坐标

color1 = (0,255,0)#重绘颜色

nColorDiff = (10,10,10)#颜色负差最大值
pColorDiff = (10,10,10)#颜色正差最大值

connectivity = 4#连通性标准

cv2.floodFill(img, mask, seed_pt, color1, nColorDiff, pColorDiff, connectivity)







cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
