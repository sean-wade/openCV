# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:45:34 2019

@author: Sean
"""

import cv2


img = cv2.imread('star.bmp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

thresh, contours, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(len(contours))

for cnt in contours:
#    center, radius = cv2.minEnclosingCircle(cnt)    #最小外接圆
#    print(center)
#    print(radius)
#    cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0,0,255), 2)
#    cv2.drawContours(img, cnt, -1, (0,255,0), 2)
#    
#    rect = cv2.fitEllipse(cnt)    #椭圆拟合，返回一个矩形对象
#    cv2.ellipse(img, rect, (0,0,255), 2, cv2.LINE_AA)
    
    
    #逼近多边形曲线
#    approx = cv2.approxPolyDP(cnt, 3, True)    #3表示精度，True表示封闭
#    cv2.drawContours(img, [approx], -1, (0,0,255), 2)
    
    #求轮廓面积及周长，可用于轮廓筛选
    area = cv2.contourArea(cnt, False)    #默认False表绝对值
    print("area : %d"%area)
    length = cv2.arcLength(cnt, True)    #True 表示封闭曲线
    print("length : %d"%length)
    print("--------><--------")
    
    if length < 300:
        cv2.drawContours(img, cnt, -1, (0,0,255), 2)




cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()