# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:47:27 2019

@author: Sean
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:34:59 2019

@author: Sean
"""
#视频检测红白色火焰，标记矩形位置

import cv2
import numpy as np


def main():
    
    cap = cv2.VideoCapture()
    cap.open('dabao.mp4')
#    cap.open('fire.mp4')
    
    cv2.namedWindow('ret')
    cv2.namedWindow('src')
     
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
#        lower = np.array([0, 0, 194])
#        upper = np.array([31, 255, 255])    #这两行是fire.mp4的火焰的HSV阈值
        
        lower = np.array([0, 153, 90])
        upper = np.array([10, 255, 255])    #这两行是大宝瓶盖阈值
        
        mask1 = cv2.inRange(hsv_img, lower, upper)
        
        img2 = cv2.bitwise_and(hsv_img, hsv_img, mask=mask1)
        
        cv2.imshow('ret', img2)
        
        blur = cv2.GaussianBlur(mask1, (5,5), 0)
        k1 = np.ones((9,9), np.uint8)
        dilate = cv2.dilate(blur, k1, iterations = 1)
        erosion = cv2.erode(dilate, k1, iterations = 1)
        
        thresh, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            if area > 22000:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
#                cv2.putText(frame, 'Fire', (x-20,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,255))
                cv2.putText(frame, 'PingGai', (x-20,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,255))
        
        cv2.imshow('src', frame)
        
        if cv2.waitKey(30)==27:
            break
#    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()






















