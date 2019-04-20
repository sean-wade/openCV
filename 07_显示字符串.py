# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:12:53 2019

@author: Sean
"""
#draw functions

import cv2
import numpy as np
img=cv2.imread("cp.bmp")
#img=np.zeros((600,600,3),np.uint8)
#cv2.line(img,(200,100),(80,500),(0,0,255),10,cv2.LINE_AA)
#cv2.circle(img,(200,200),100,(0,255,0),-1)
cv2.rectangle(img,(67,110),(400,210),(112,228,255),5)
#cv2.ellipse(img,(450,500),(100,20),-90,0,270,(222,255,0),-1)

pts=np.array([[500,100],[200,20],[40,200],[180,200],[190,112]],np.int32)
#cv2.fillPoly(img,[pts],(0,255,0),cv2.LINE_AA)
#cv2.polylines(img,[pts],False,(0,0,255),10)
font=cv2.FONT_ITALIC
cv2.putText(img,'Here',(100,200),font,4,(255,255,0))

cv2.imshow("Car Licence",img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

