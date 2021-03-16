import cv2
import sys

if len(sys.argv) ==  2:
	if sys.argv[1] == '--webcam':
		video = cv2.VideoCapture(0)
		if not video.isOpened():
			print("Built in webcam does not exist. Exiting ...")
			exit()
	elif sys.argv[1] == '--ext':
		video = cv2.VideoCapture(1)
		if not video.isOpened():
			print("Built in webcam does not exist. Exiting ...")
			exit()
	else :
		video = cv2.VideoCapture(sys.argv[1])
		if not video.isOpened():
			print("Video does not exist. Exiting ...")
			exit()
else:
	print("Not enough arguments. Exiting ...")
	exit()

tracker = cv2.TrackerCSRT_create()

ok, img = video.read()
if not ok:
	print("Cannot read video file")
	exit()

box = cv2.selectROI("Tracker", img, False)
tracker.init(img, box)

def drawBox(img, box):
	x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
	cv2.rectangle(img, (x,y), ((x+w), (y+h)), (0, 255, 0), 3, 1)

while True:
	ok, img = video.read()
	if not ok:
		print("Cannot read video file")
		exit()

	ok, box = tracker.update(img)

	if ok:
		drawBox(img, box)
	else:
		cv2.putText(img, "Object Lost", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

	cv2.imshow("Tracker", img)

	if cv2.waitKey(40) == 27:
		break