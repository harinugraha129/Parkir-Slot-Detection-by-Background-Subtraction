import cv2
import numpy as np


from collections import Counter
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
# cap = cv2.VideoCapture("footage.mp4")
# start_frame_number = 100
# cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
_, first_frame = cap.read()

first_frame = resize(first_frame)
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

list_marker = [ 
                [(230,180), (330, 276)], 
                [(342,180), (442, 276)], 
                [(454,180), (555, 276)],
                [(565,180), (665, 276)],
                [(677,180), (776, 276)]
                                        ]
marker = []

count = 0

while True:
    count += 1
    if (count%60)==0:
        print(count%60)
        # continue


        keisi = 0
        kosong = 0
        _, frame = cap.read()
        frame =resize(frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
        
        thicness = 5
        # cv2.imshow("First frame", first_frame)
        for marker in list_marker:
            frame = cv2.rectangle(frame, marker[0], marker[1], (0,255,0), thicness)
            marker_croped = difference[marker[0][1]:marker[1][1], marker[0][0]:marker[1][0]]
            marker_croped = list(np.concatenate(marker_croped).flat)
            minimum_255 = int(0.58*len(marker_croped))
            pixcel = Counter(marker_croped)

            if pixcel[255]>minimum_255:
                keisi += 1
            else:
                kosong += 1

        result = "Keisi "+str(keisi)+", Kosong "+str(kosong)+", Total-slot "+str(len(list_marker))
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, result, (10, 100), font, 1, (0, 255, 255), 3, cv2.LINE_AA)

        cv2.imshow("Frame", frame)
        # cv2.imshow("difference", difference)
        # cv2.imshow("marker", marker_croped)
        # cv2.imshow("marker2", marker_croped2)

        key = cv2.waitKey(1)
        if key == 27:
            break
cap.release()
cv2.destroyAllWindows()
