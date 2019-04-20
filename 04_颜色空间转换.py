# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:42:33 2019

@author: Sean
"""
import cv2
import numpy as np

img=cv2.imread(r'sdty.png')
img2=img.copy()

#img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

##img=np.zeros((600,400,3),np.uint8)
#img=np.eye(5,4)
##img=np.ones((600,400,3),np.uint8)
##img*=255
cv2.imshow("IMG",img)
cv2.imshow("IMG2",img2)
#print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()