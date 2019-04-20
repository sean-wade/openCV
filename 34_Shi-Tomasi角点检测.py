# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:02:00 2019

@author: Sean
"""

import cv2
import numpy as np

img = cv2.imread('yuan.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#构造参数字典
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 5,
                      blockSize = 10)
"""
字典作为参数传入，相当于参数是：
                      maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 10,
                      blockSize = 5def test(*args):

* 的含义又要有所不同，在这里 *args 表示把传进来的位置参数都装在元组 args = (1,2,3)里面。
比如调用test(*args) 的话， args 的值就是 (1, 2, 3) 
"""
corners = cv2.goodFeaturesToTrack(gray, mask=None, **feature_params)

print('conerNum = '+str(len(corners)))

for i in range(0, len(corners)):
    cv2.circle(img, tuple(corners[i][0]), 5, (0,255,0),2)

cv2.imshow('res', img)

cv2.waitKey(0)
cv2.destroyAllWindows()