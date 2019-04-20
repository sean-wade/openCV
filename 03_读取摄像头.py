# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:01:15 2019

@author: Sean
"""

import cv2

cap= cv2.VideoCapture("C:/Users/Sean/Desktop/fire.mp4")
i=1
if cap.isOpened():
    while True:
        ret,frame=cap.read()
        if ret==False:
            break
        cv2.imshow("Fire",frame)
        #cv2.imwrite("C:/Users/Sean/Desktop/fire/"+str(i)+".jpg",frame)
        #cv2.imwrite("C:/Users/Sean/Desktop/fire/{}.jpg".format(str(i)),frame)
        cv2.imwrite("C:/Users/Sean/Desktop/fire/%s.jpg"%str(i),frame)
        i+=1
        if cv2.waitKey(10)&0XFF==27:
            break
cv2.destroyAllWindows()
cap.release()
        