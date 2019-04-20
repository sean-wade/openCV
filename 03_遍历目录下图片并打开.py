# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:41:14 2019

@author: Sean
"""
from os import listdir
import cv2
#import glob

filepath="fire"
i=1
for filename in listdir(filepath):
#    print(filename)
    if filename[-3:]=='jpg' or filename[-3:]=='png':
#        print(filename)
        filename=filepath+r'/'+filename
        print(filename)
        img=cv2.imread(filename)
        if img is None:
            break
        cv2.imshow("Desktop"+str(i),img)
        cv2.waitKey(20)
        i+=1
         
cv2.waitKey(0)
cv2.destroyAllWindows()
        
        

#for item in glob.glob("C:/Users/Sean/Desktop/*.jpg"):
#    print(item)