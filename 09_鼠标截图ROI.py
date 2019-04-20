# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:10:08 2019

@author: Sean
"""

import cv2
import numpy as np
import math

flag=False    #标志位,鼠标左键是否按下
x1=y1=0

def screenShot(event,x,y,flags,param):
    global x1,y1,flag,img,temp
    if event==cv2.EVENT_LBUTTONDOWN:
        flag=True
        x1=x
        y1=y
    elif event==cv2.EVENT_MOUSEMOVE:
        if flag==True:
            img=temp.copy()   #原图复制，把绘制矩形清空
            cv2.rectangle(img,(x1,y1),(x,y),(0,0,255),2)
#            cv2.circle(img,(int((x+x1)/2),int((y+y1)/2)),int(math.sqrt((x-x1)**2+(y-y1)**2)/2),(255,255,0),2)
    elif event==cv2.EVENT_LBUTTONUP:
        flag=False
        if x1==x and y1==y:
            img=temp.copy()
        ROI=temp[y1:y,x1:x]
        cv2.imshow('ROI',ROI)
        cv2.imwrite('C:/Users/Sean/Desktop/ROI.png',ROI)
#        cv2.rectangle(img,(x1,y1),(x,y),(0,255,0),2)


img=cv2.imread("sdty.png")
temp=img.copy()

cv2.namedWindow('ScreenShot')
cv2.setMouseCallback('ScreenShot',screenShot)

while(1):
    cv2.imshow('ScreenShot',img)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()