import cv2 as cv
import numpy as np
import winsound
a=cv.VideoCapture(0);
ret,frame=a.read();
previous_frame=frame;
while True:
    ret,frame=a.read();
    if not ret:
        break
    current_frame=frame;
    diff=cv.absdiff(current_frame,previous_frame);
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY);
    _, th=cv.threshold(gray,100,255,cv.THRESH_BINARY);
    ans=np.sum(th==255);
    alarm= False;
    if ans>10000 and not alarm:
        cv.rectangle(current_frame,(100,100),(200,250),(0,0,255),5)
        cv.imwrite("manu.jpg",current_frame)
        winsound.Beep(1000,100)
    cv.imshow("MOTION DETECTOR",current_frame);
    previous_frame=current_frame;
    if cv.waitKey(1) & 0xFF== ord('q'):
        break;
a.release();
cv.destroyAllWindows();