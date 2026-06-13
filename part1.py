import cv2 as cv
import numpy as np
a=cv.VideoCapture(0);
ret,frame=a.read();
previous_frame=frame;
while True:
    ret,frame=a.read();
    current_frame=frame;
    diff=cv.absdiff(current_frame,previous_frame);
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY);
    _, th=cv.threshold(gray,100,255,cv.THRESH_BINARY);
    ans=np.sum(th==255);
    if ans>10000:
        print("MOTION DETECTED");
    cv.imshow("MOTION DETECTOR",th);
    previous_frame=current_frame;
    if cv.waitKey(1) &  0xFF== ord('q'):
        break;
a.release();
cv.destroyAllWindows();