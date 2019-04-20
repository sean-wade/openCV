# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:39:20 2019

@author: Sean
"""

import cv2

temp=cv2.imread("pg.jpg")
w,h=temp.shape[1],temp.shape[0]


cap=cv2.VideoCapture()
cap.open("dabao.mp4")


cv2.namedWindow('Dabao')

while True:
    ret,frame=cap.read()
    if ret==False:
        break
    res=cv2.matchTemplate(frame,temp,cv2.TM_CCORR_NORMED)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    left_top=max_loc
    right_bottom=(max_loc[0]+w,max_loc[1]+h)
    cv2.rectangle(frame,left_top,right_bottom,(0,255,0),2)
    cv2.putText(frame,'PingGai',left_top,1,cv2.FONT_HERSHEY_COMPLEX,(0,0,255),2)
    
    cv2.imshow('Dabao',frame)
    if cv2.waitKey(40)==27:
        break
    
cv2.destroyAllWindows()
cap.release()