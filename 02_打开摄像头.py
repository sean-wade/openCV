# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:52:30 2019

@author: Sean
"""
import cv2
#VideoCapture 打开视频或者摄像头取图像，跟声音无关

#cap = cv2.VideoCapture("https://www.bilibili.com/video/av39547327")
#if cap.isOpened():
#    while True:
#        ret,frame=cap.read()
#        if ret==False:
#            break
#        cv2.imshow("年轻气盛",frame)
#        if cv2.waitKey(50) & 0XFF==27:
#            cv2.imwrite("C:/Users/Sean/Desktop/1.bmp",frame)
#            cv2.destroyAllWindows()
#            break
#else:
#      print("Open failed!")  
    
#cap=cv2.VideoCapture()
#cap.open(0)
#if cap.isOpened():
#    while True:
#        ret,frame=cap.read()    #读取一帧
#        if ret==False:  #判断读取是否成功
##        if frame is None:    也可以判断读取是否成功
#            break
#        frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#转换为HSV
##        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   转换为灰度
#        cv2.imshow("SXT",frame_hsv)
#        if cv2.waitKey(50)&0XFF==27:
#            cv2.imwrite("C:/Users/Sean/Desktop/1.jpg",frame_hsv)
#            break
#cap.release()#释放摄像头资源，但是在我的笔记本上灯还没关闭
#cv2.destroyAllWindows()

#保存摄像头帧到视频文件
cap=cv2.VideoCapture()
cap.open(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID') #设置编码方式，也可以直接写-1
out=cv2.VideoWriter("C:/Users/Sean/Desktop/a.avi",fourcc,10.0,(640,480))
if cap.isOpened():
    while True:
        ret,frame=cap.read()
        if ret==False:
            print("Done!")
            break
        cv2.imshow("SXT",frame)
        out.write(frame)
        if cv2.waitKey(50)&0xFF==27:
            break

cv2.destroyAllWindows()
cap.release()
out.release()
