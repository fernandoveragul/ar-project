import cv2
img = cv2.imread("")
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(img)
print(f"QRCode data:\n{data}")