import cv2
img = cv2.imread("qrcode6.jpg")
detector = cv2.QRCodeDetector()
data, _, _ = detector.detectAndDecode(img)
print(f"QRCode data:\n{data}")