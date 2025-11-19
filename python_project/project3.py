import cv2
from pyzbar.pyzbar import decode

camera = cv2.VideoCapture(0)
print("QR Scanner running... press ESC to quit")
previous_text = None

while True:

  ret, frame = camera.read()
  if not ret:
    print("Unable to access camera")
    break

  results = decode(frame)

  for r in results:
    text = r.data.decode("utf-8")
    if text != previous_text:
      print("Scanned:", text)
      previous_text = text

    pts = r.polygon

    for idx in range(len(pts)):
      p1 = pts[idx]
      p2 = pts[(idx + 1) % len(pts)]
      cv2.line(frame, p1, p2, (0, 0, 255), 2)

  cv2.imshow("QR Scanner", frame)
  if cv2.waitKey(1) == 27:
    break

camera.release()
cv2.destroyAllWindows()
