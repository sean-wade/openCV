# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:22:23 2019

@author: Sean
"""

import cv2

i=1
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('C:/Users/Sean/Desktop/out.avi',fourcc,25.0,(1280,720))
while True:
    frame=cv2.imread("C:/Users/Sean/Desktop/fire/{}.jpg".format(str(i)))
    if frame is None:
        break 
    out.write(frame)
    i+=1
out.release()
