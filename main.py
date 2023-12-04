import pyautogui
import numpy
import cv2
from cv2 import VideoWriter

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0
out = VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = numpy.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Live", frame)
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()

