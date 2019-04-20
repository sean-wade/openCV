# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:44:12 2019

@author: Sean
"""

# =============================================================================
# 运动物体检测相关内容
# 1、背景减法 
# 2、帧差法
# 基本步骤： 原图-背景-阈值处理-去除噪声(腐蚀滤波)-膨胀连通-查找轮廓-外接矩形(椭圆)
# =============================================================================

import cv2
import numpy as np

#下面为保存bike.avi中的几张图
#cap = cv2.VideoCapture()
#cap.open('bike.avi')
#cv2.namedWindow('Bike')
#i=0
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    cv2.imshow('Bike', frame)
#    if cv2.waitKey(66)==ord('q'):
#        break
#    if i%10==0:
#        cv2.imwrite('bike\%d.jpg'%i, frame)
#    i = i+1
#cap.release()

    
img1 = cv2.imread('bike/10.jpg')
img2 = cv2.imread('bike/50.jpg')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)
cv2.imshow('diff', diff)

ret, thresh = cv2.threshold(diff, 60, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)

k1 = np.ones((2,2), np.uint8)
k2 = np.ones((9,9), np.uint8)

erode = cv2.erode(thresh, k1)
cv2.imshow('erode', erode)

dilate = cv2.dilate(erode, k2)
cv2.imshow('dilate', dilate)

thresh, contours, hierarchy = cv2.findContours(dilate, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img2, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('Move', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()





