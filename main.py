import cv2
import time
from plyer import notification

def leer_qr(path_qr):
    img=cv2.imread(path_qr)
    detector=cv2.QRCodeDetector()
    data=detector.detectAndDecode(img)
    return data[0]

message=leer_qr("frame.png")
notification.notify(
    title="This is a python test!!",
    message=str(message),
    timeout=10
)

time.sleep(10)