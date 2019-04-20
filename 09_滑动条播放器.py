# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 08:54:11 2019

@author: Sean
"""

import cv2


def videoControl(framePos):
    global cap
    cap.set(cv2.CAP_PROP_POS_FRAMES,framePos)

font=cv2.FONT_HERSHEY_COMPLEX_SMALL

cap=cv2.VideoCapture("car.mp4")

flag=0

if cap.isOpened():
    flag=1
else:
    flag=0

cv2.namedWindow('car')
frameCount=cap.get(cv2.CAP_PROP_FRAME_COUNT)
cv2.createTrackbar('framePos','car',0,int(frameCount),videoControl)
fps=cap.get(cv2.CAP_PROP_FPS)


while(1):
    position=cap.get(cv2.CAP_PROP_POS_FRAMES)
    cv2.setTrackbarPos('framePos','car',int(position))
    
    ret,frame=cap.read()
    cv2.putText(frame,"FPS:%0.1f/s"%fps,(10,20),font,1.1,(0,255,0),2)
    if ret==False:
        break
    cv2.imshow('car',frame)
    if cv2.waitKey(int(1000/fps))==27:
        break
    
cap.release()
cv2.destroyAllWindows()