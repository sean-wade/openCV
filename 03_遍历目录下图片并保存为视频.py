# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 18:10:07 2019

@author: Sean
"""
import cv2
from os import listdir

filepath="fire"
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('C:/Users/Sean/Desktop/a.avi',fourcc,2.0,(640,480))

for filename in listdir(filepath):
    if filename[-3:]=='jpg' or filename[-3:]=='png':
        filename=filepath+r'/'+filename
        img=cv2.imread(filename)
        if img is None:
            break
        img=cv2.resize(img,(640,480),interpolation=cv2.INTER_CUBIC)
        out.write(img)
        
out.release()

        

