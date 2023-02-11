import cv2
import numpy as np
cap = cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2(300,400, False)
while(True):
    success, frame = cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow("fgbg", fgmask)

    count=np.count_nonzero(fgmask)
    if count>5000:
        print("xyz")

    key=cv2.waitKey(1) & 0xff
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()