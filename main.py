import cv2

def leer_qr(path_qr):
    img=cv2.imread(path_qr)
    detector=cv2.QRCodeDetector()
    data=detector.detectAndDecode(img)
    return data

print(leer_qr("QR-example.png"))