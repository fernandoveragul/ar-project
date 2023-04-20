import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
myData = None
while myData is None:
    req, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts], True,(255,0,0,5))
        print(myData)
    cv2.imshow("img", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()