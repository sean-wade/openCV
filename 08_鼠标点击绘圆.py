# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:04:18 2019

@author: Sean
"""

import cv2
import numpy as np

#for event in dir(cv2):
#    if 'EVENT' in event:
#        print(event)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,255,0),2)

img=np.zeros((600,600,3),np.uint8)

cv2.namedWindow("MouseClickDraw")
cv2.setMouseCallback("MouseClickDraw",draw_circle)

while(1):
    cv2.imshow("MouseClickDraw",img)
    if cv2.waitKey(1)&0xff==27:
        break
cv2.destroyAllWindows()