# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# https://piofthings.net/blog/opencv-baby-steps-4-building-a-hsv-calibrator

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import pickle
import serial
import _thread
import sys
from pynput.keyboard import Key, Listener
import random


# --------------parameters------------------------
automode = 'autoDrive0'  # 'autoDrive0' , 'autoDrive1' , 'autoDrive2' , 'none'
link = 0  # 0, 'http://192.168.0.106:1224/video' , 'car01.mp4'
line = False
flip = False
inner = 60
outer = 0
writeCommand = False
verbose = True
portName = 'COM6'


# -------------------- definitions for automated car control --------------------------


# storing directions
forward = False
backward = False
left = False
right = False


# movements
# stop
def stop():
    global forward
    global backward
    global left
    global right
    forward = False
    backward = False
    left = False
    right = False
    signal = '#FWR0\n'
    write(signal)
    signal = '#RGH0\n'
    write(signal)
    signal = '#BAC0\n'
    write(signal)
    signal = '#LEF0\n'
    write(signal)

    if verbose:
        print('stop')


# timed
def goFwd(time):
    global forward
    global backward
    global left
    global right
    forward = True
    backward = False
    left = False
    right = False
    signal = '#FWRD\n'
    write(signal)

    time.sleep(time)

    stop()


def goRght(time):
    global forward
    global backward
    global left
    global right
    forward = True
    backward = False
    left = False
    right = True
    signal = '#FWRD\n'
    write(signal)
    signal = '#RGHT\n'
    write(signal)

    time.sleep(time)

    stop()


def goLft(time):
    global forward
    global backward
    global left
    global right
    forward = True
    backward = False
    left = True
    right = False
    signal = '#FWRD\n'
    write(signal)
    signal = '#LEFT\n'
    write(signal)

    time.sleep(time)

    stop()


def goBck(time):
    global forward
    global backward
    global left
    global right
    forward = False
    backward = True
    left = False
    right = False
    signal = '#BACK\n'
    write(signal)

    time.sleep(time)

    stop()


def bckLft(time):
    global forward
    global backward
    global left
    global right
    forward = False
    backward = True
    left = True
    right = False
    signal = '#BACK\n'
    write(signal)
    signal = '#LEFT\n'
    write(signal)

    time.sleep(time)

    stop()


def bckRght(time):
    global forward
    global backward
    global left
    global right
    forward = False
    backward = True
    left = False
    right = True
    signal = '#BACK\n'
    write(signal)
    signal = '#RGHT\n'
    write(signal)

    time.sleep(time)

    stop()


# infinite
def goRghtInf():
    global forward
    global backward
    global left
    global right
    forward = True
    backward = False
    left = False
    right = True
    stop()
    signal = '#FWRD\n'
    write(signal)
    signal = '#RGHT\n'
    write(signal)

    if verbose:
        print('goRghtInf')


def goLftInf():
    global forward
    global backward
    global left
    global right
    forward = True
    backward = False
    left = True
    right = False
    stop()
    signal = '#FWRD\n'
    write(signal)
    signal = '#LEFT\n'
    write(signal)

    if verbose:
        print('goLftInf')


def bckLftInf():
    global forward
    global backward
    global left
    global right
    forward = False
    backward = True
    left = True
    right = False
    stop()
    signal = '#BACK\n'
    write(signal)
    signal = '#LEFT\n'
    write(signal)

    if verbose:
        print('bckLftInf')


def bckRghtInf():
    global forward
    global backward
    global left
    global right
    forward = False
    backward = True
    left = False
    right = True
    stop()
    signal = '#BACK\n'
    write(signal)
    signal = '#RGHT\n'
    write(signal)

    if verbose:
        print('bckRghtInf')


def goFwdInf():
    global forward
    global backward
    global left
    global right

    stop()

    forward = True
    backward = False
    left = False
    right = False

    signal = '#FWRD\n'
    write(signal)

    if verbose:
        print('goFwdInf')


def bckBckInf():
    global forward
    global backward
    global left
    global right

    stop()

    forward = False
    backward = True
    left = False
    right = False

    signal = '#BACK\n'
    write(signal)

    if verbose:
        print('bckBckInf')


# quasi random function chooses a random direction for the car
def direction():
    rnd = random.randint(1, 6)
    if rnd == 1:
        goFwdInf()
    elif rnd == 2:
        goRghtInf()
    elif rnd == 3:
        goLftInf()
    elif rnd == 4:
        bckBckInf()
    elif rnd == 5:
        bckRghtInf()
    elif rnd == 6:
        bckLftInf()


# reverse fuction reverses direction (expl.: fwrd left -> bck right)
def reverse():
    if forward == True:
        if left == True:
            bckRghtInf()
        elif right == True:
            bckLftInf()
        else:
            bckBckInf()
    else:
        if left == True:
            goRghtInf()
        elif right == True:
            goLftInf()
        else:
            goFwdInf()


# quasi random function chooses a random direction for the car - no straith forward / back
# startoff for automode 2 (only starts if automode = automode2)
def auto2Direction():
    if automode == 'autoDrive2':
        rnd = random.randint(1, 4)

        if rnd == 1:
            goRghtInf()
        elif rnd == 2:
            goLftInf()
        elif rnd == 3:
            bckLftInf()
        else:
            bckRghtInf()


# in automode 2 reverts direction (every time when hits wall)
# if wall, reverse
def auto2DirectionChange():
    if automode == 'autoDrive2':
        reverse()


# try to open serial port
try:
    ser1 = serial.Serial(portName, 9600)  # open serial port
    print(ser1.name)  # check which port was really used
    # ser.write('#STAR\n'.encode('utf-16'))     # write a string
    time.sleep(2)
    print('well slept ;) \n')
#    _thread.start_new_thread(ControlListener, ())

# if there is no serial port, write out commands
except:
    print(portName + ' port is not available \n')


#    _thread.start_new_thread(ControlListenerTest, ())

# write function (writes to port if available, else prints the message out)
def write(signal):
    try:
        ser1.write(signal.encode())
    except:
        if writeCommand:
            print(signal)


# -------------------- end of definitions for acc --------------------------

# define color boundaries if neccesary
def detectColor(colorToDetect):
    def callback(x):
        pass

    cap = cv2.VideoCapture(link)
    cv2.namedWindow('image')

    f = open(str(colorToDetect) + '.pckl', 'rb')
    obj = pickle.load(f)
    f.close()
    ilowH = obj[0]
    ihighH = obj[1]
    ilowS = obj[2]
    ihighS = obj[3]
    ilowV = obj[4]
    ihighV = obj[5]

    # create trackbars for color change
    cv2.createTrackbar('lowH', 'image', ilowH, 179, callback)
    cv2.createTrackbar('highH', 'image', ihighH, 179, callback)

    cv2.createTrackbar('lowS', 'image', ilowS, 255, callback)
    cv2.createTrackbar('highS', 'image', ihighS, 255, callback)

    cv2.createTrackbar('lowV', 'image', ilowV, 255, callback)
    cv2.createTrackbar('highV', 'image', ihighV, 255, callback)

    while (True):
        # grab the frame
        ret, frame = cap.read()
        if flip:
            frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, width=600)

        # get trackbar positions
        ilowH = cv2.getTrackbarPos('lowH', 'image')
        ihighH = cv2.getTrackbarPos('highH', 'image')
        ilowS = cv2.getTrackbarPos('lowS', 'image')
        ihighS = cv2.getTrackbarPos('highS', 'image')
        ilowV = cv2.getTrackbarPos('lowV', 'image')
        ihighV = cv2.getTrackbarPos('highV', 'image')

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([ilowH, ilowS, ilowV])
        higher_hsv = np.array([ihighH, ihighS, ihighV])
        mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

        frame = cv2.bitwise_and(frame, frame, mask=mask)
        # show thresholded image
        cv2.imshow('detected', frame)
        k = cv2.waitKey(100) & 0xFF  # large wait time to remove freezing
        if k == 115:
            print('save')
            obj = [ilowH, ihighH, ilowS, ihighS, ilowV, ihighV]
            f = open(str(colorToDetect) + '.pckl', 'wb')
            pickle.dump(obj, f)
            f.close()
            break
        if k == 113 or k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    return


start = input("enter g + enter to set values for green, or enter to continue \n")
if start == "g":
    colorToDetect = 'green'
    detectColor(colorToDetect)
start = input("enter b + enter to set values for blue, or enter to continue \n")
if start == "b":
    colorToDetect = 'blue'
    detectColor(colorToDetect)

# load color boundaries from pickle
f = open('green.pckl', 'rb')
obj = pickle.load(f)
f.close()
greenLower = (obj[0], obj[2], obj[4])
greenUpper = (obj[1], obj[3], obj[5])
f = open('blue.pckl', 'rb')
obj = pickle.load(f)
f.close()
blueLower = (obj[0], obj[2], obj[4])
blueUpper = (obj[1], obj[3], obj[5])

# lenght of storing previous positions (used for tracing line)
buffer = 64
pts = deque(maxlen=buffer)
pts2 = deque(maxlen=buffer)
pts3 = deque(maxlen=buffer)

# set capture object
vs = cv2.VideoCapture(link)

# allow the camera or video file to warm up
time.sleep(2.0)


# when called, gets the centerpoint of the object
# also, creates the tracking line
def trackObject(Lower, Upper, pts, i):
    mask = cv2.inRange(hsv, Lower, Upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 1:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # update the points queue
    pts.appendleft(center)

    if line:
        # loop over the set of tracked points
        for i in range(1, len(pts)):
            # if either of the tracked points are None, ignore
            # them
            if pts[i - 1] is None or pts[i] is None:
                continue

            # otherwise, compute the thickness of the line and
            # draw the connecting lines
            thickness = int(np.sqrt(buffer / float(i + 1)) * 2.5)
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    return center


# switch for getting picture measurements only once
switch = True

# these checkpoints are switches, and they are checking if the car has already went through a wall or not
# they are set to false when cross the border, and back to true again when go back
checkpointBravo = True  # for the inner border
checkpointCharlie = True  # for the outer border

# startoff for automode 2 (only starts if automode = automode2)
auto2Direction()

freeToGo = True
betweenTheBars = False


# when automode 1 is on, starts a paralell thread, which gives random directions in every 1-6 sec
# def rnd direction with while
def rndDirWhile():
    while True:
        if betweenTheBars == False:
            direction()
            time.sleep(random.randint(1, 6))


if automode == 'autoDrive1':
    _thread.start_new_thread(rndDirWhile, ())

i = 1
# main loop
while True:
    # grabs frame, then converts it
    # grab the current frame
    frame = vs.read()

    # handle the frame from VideoCapture or VideoStream
    frame = frame[1]  # if args.get("video", False) else frame

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # getting picture measurements
    if switch:
        height, width, channels = frame.shape
        print(str(int(width)) + ' ' + str(int(height)))
        switch = False
        # rectangle 1 dimensions (inner wall)
        pt1x = int(inner)
        pt1y = int(inner)
        pt2x = int(width - inner)
        pt2y = int(height - inner)

        # rectangle 2 dimensions (outer wall)
        pt1bx = int(outer)
        pt1by = int(outer)
        pt2bx = int(width - outer)
        pt2by = int(height - outer)

    # drawing borders
    cv2.rectangle(frame, (pt1x, pt1y), (pt2x, pt2y), (0, 255, 0), 2)
    cv2.rectangle(frame, (pt1bx, pt1by), (pt2bx, pt2by), (0, 0, 255), 2)

    # getting the car position (center of blue and center of green
    center = trackObject(blueLower, blueUpper, pts, 1)
    # center2 = trackObject(greenLower, greenUpper, pts2, 1)

    if (center is not None):
        # sys.stdout.write("\r The coordinates of blue are %i : %i" % (center[0], center[1]))
        sys.stdout.flush()

        # check if outside the boundaries
        if center[0] < pt1x or center[0] > pt2x or center[1] < pt1y or center[1] > pt2y:
            if checkpointBravo == True:
                # crossed inner border!!!

                # automode 0
                if automode == 'autoDrive0':
                    # print(str(forward) + ' ' + str(backward) + ' \n')
                    if forward == True:
                        bckBckInf()
                    else:
                        goFwdInf()

                # when first here with auto mode 1, go left
                if automode == 'autoDrive1':
                    if freeToGo == True and betweenTheBars == False:
                        goRghtInf()
                        freeToGo = True
                        betweenTheBars = True

                # auto drive 2 (simply changes direction when hits wall)
                # if wall, reverse
                auto2DirectionChange()
                #
                # print('\n inside border crossed \n')
                checkpointBravo = False

            # check if outside outer boundaries
            if center[0] < pt1bx or center[0] > pt2bx or center[1] < pt1by or center[1] > pt2by:
                if checkpointCharlie == True:
                    # crossed outer border!!!

                    # automode 0
                    if automode == 'autoDrive0':
                        stop()

                    # auto drive 1 - revert direction vhen outer wall
                    if automode == 'autoDrive1':
                        reverse()
                        FreeToGo = False

                    # auto drive 2 (simply changes direction when hits wall)
                    # if we are in auto drive2 we should never get here...
                    # if wall, reverse
                    auto2DirectionChange()
                    #
                    # print('\n outside border crossed \n')
                    checkpointCharlie = False

            else:  # the else is for the previous if (tested)
                checkpointCharlie = True

        else:  # car is within boundaries

            # when auto mode 1 if free to go == false -> reverse, else let it go
            if automode == 'autoDrive1':
                if freeToGo == False:
                    reverse()
                    freeToGo = True
                else:
                    betweenTheBars = False

            checkpointBravo = True

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

    # automode 0
    if i == 1 and automode == 'autoDrive0':
        goFwdInf()
    i = i + 1

# close all windows
stop()
cv2.destroyAllWindows()
