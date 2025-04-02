import cv2
from PIL import Image
from utility import get_limits


yellow=[0,255,255]
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsvimage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    ll,ul=get_limits(color=yellow)

    mask=cv2.inRange(hsvimage,ll,ul)

    cv2.imshow('frame',mask)

    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        a,b,c,d=bbox
        frame=cv2.rectangle(frame,(a,b),(c,d),(0,255,0),5)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()