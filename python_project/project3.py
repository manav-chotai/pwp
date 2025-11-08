import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
last_data = None

print("Scanning for QR Code. Press 'ESC' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    for barcode in decode(frame):
        data = barcode.data.decode('utf-8')

        if data != last_data:
            print("QR Code data:", data)
            last_data = data

        points = barcode.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        for i in range(len(hull)):
            cv2.line(frame, hull[i], hull[(i+1) % len(hull)], (255, 0, 0), 3)

    cv2.imshow("QR Code Scanner", frame)

    key = cv2.waitKey(10)
    if key == 27 or key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
