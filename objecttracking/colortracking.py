import cv2
import numpy as np

def get_frame(cap,scaling_factor):
    ret,frame= cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor,
    fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame
            
if __name__=="__main__":
    cap=cv2.VideoCapture('http://192.168.1.100:8080/videofeed')
    scaling_factor=0.5
    
    
    while True:
        frame=get_frame(cap,scaling_factor)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower=np.array([60,100,100])
        upper=np.array([180,255,255])
        
        mask=cv2.inRange(hsv,lower,upper)
        
        res=cv2.bitwise_and(frame,frame,mask=mask)
        res=cv2.medianBlur(res,5)
        cv2.imshow('Original Image', frame)
        cv2.imshow('Color Detector', res)
        
        c= cv2.waitKey(5)
        if c==27:
            break
    cv2.destroyAllWindows()