import cv2
import numpy as np

def resize(img):
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

# cap = cv2.VideoCapture("highway.mp4")
cap = cv2.VideoCapture("foo.mp4")
_, first_frame = cap.read()

first_frame = resize(first_frame)
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    _, frame = cap.read()
    frame =resize(frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    
    thicness = 5
    # cv2.imshow("First frame", first_frame)
    frame = cv2.rectangle(frame, (230,180), (330, 276), (0,255,0), thicness)
    frame = cv2.rectangle(frame, (342,180), (442, 276), (0,255,0), thicness)
    frame = cv2.rectangle(frame, (454,180), (555, 276), (0,255,0), thicness)
    frame = cv2.rectangle(frame, (565,180), (665, 276), (0,255,0), thicness)
    frame = cv2.rectangle(frame, (677,180), (776, 276), (0,255,0), thicness)
    cv2.imshow("Frame", frame)
    # cv2.imshow("difference", difference)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()