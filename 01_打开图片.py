# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:10:17 2018

@author: Sean
"""
import cv2

img = cv2.imread(r"C:\Users\Sean\Desktop\sdty.png")
cv2.imshow("HaHa",img)
cv2.waitKey(0)
cv2.destroyAllWindows()