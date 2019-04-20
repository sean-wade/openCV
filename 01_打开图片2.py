import cv2
#import numpy as np

img=cv2.imread('C:/Users/Sean/Desktop/sdty.png',cv2.IMREAD_COLOR)
if img is None:
    print("Error,cound not find the image!")
else:
    print("Open Success")
#    cv2.namedWindow("IMGshow",cv2.WINDOW_FREERATIO)
#    cv2.imshow("IMGshow",img)
    print(img.shape[0])
    print(img.shape[1])
    print(img.shape[2])
    print(img.dtype)
    print(img)
    
#    while True:
#        if cv2.waitKey(0)==ord(' '):
#            cv2.destroyAllWindows()
#            cv2.imwrite("C:/Users/Sean/Desktop/sdtyhb.jpg",img)
#            break
#        else:
#            print("Type ' ' to quit!")
        
        
