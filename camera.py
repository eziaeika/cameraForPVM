# import cv2
#
# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(1)
#
# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False
#
# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")



import numpy as np
import cv2

video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(2)



def make_1080p():
    video_capture_0.set(3, 1920)
    video_capture_0.set(4, 1080)

def make_720p():
    video_capture_0.set(3, 1280)
    video_capture_0.set(4, 720)

def make_480p():
    video_capture_0.set(3, 640)
    video_capture_0.set(4, 480)
    video_capture_1.set(3, 640)
    video_capture_1.set(4, 480)



def change_res(width, height):
    video_capture_0.set(3, width)
    video_capture_0.set(4, height)

make_480p()




while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()

    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 0', frame0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()