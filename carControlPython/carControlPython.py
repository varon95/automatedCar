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

global isRecording
isRecording = False
global lista 
lista = []

global forwTrue
global backTrue
global rightTrue
global leftTrue

forwTrue  = False
backTrue  = False
rightTrue = False
leftTrue  = False

def play():
    memberNumber = 0
    loopTime = 0
    startTime = time.time()
    #go until we reach the last character on the list
    while memberNumber<len(lista):
        #if we reach the time of a list member, "play" the listmember
        if lista[memberNumber][0] == loopTime:
          write(lista[memberNumber][1])
          hundredthSec()
          #go to next list member
          memberNumber +=1
        loopTime += 1
        #sleep, so total time = 10ms
        time.sleep(0.01 - ((time.time() - startTime) % 0.01))

def playReverse():
    #memberNumber = 0
    memberNumber = -1
    #loopTime = 0
    loopTime = lista[-1][0] + 100
    startTime = time.time()
    #go until we reach the last character on the list
    while abs(memberNumber)<=len(lista):
        #if we reach the time of a list member, "play" the listmember
        if lista[memberNumber][0] == loopTime:
          signal = lista[memberNumber][1]
          write(reverseSignal(signal))
          hundredthSec()
          #go to next list member
          #memberNumber +=1
          memberNumber -=1
        #loopTime += 1
        loopTime -= 1
        #sleep, so total time = 10ms
        time.sleep(0.01 - ((time.time() - startTime) % 0.01))

def reverseSignal(signal):
    if signal == '#FWRD\n' :
        signal = '#FWR0\n'
    elif signal == '#BACK\n' :
        signal = '#BAC0\n'
    elif signal == '#LEFT\n' :
        signal = '#LEF0\n'
    elif signal == '#RGHT\n' :
        signal = '#RGH0\n'

    elif signal == '#FWR0\n' :
        signal = '#FWRD\n'
    elif signal == '#BAC0\n' :
        signal = '#BACK\n'
    elif signal == '#LEF0\n' :
        signal = '#LEFT\n'
    elif signal == '#RGH0\n' :
        signal = '#RGHT\n'

    return signal



def write(signal):
    try:
        ser1.write(signal.encode())
    except:
        print(signal)


def hundredthSec():
    return (int(round((time.time()-startTime) * 100)))

def record(signal):
    if isRecording == True:
       lista.append([hundredthSec(),signal])

def on_press(key):
    global forwTrue
    global backTrue
    global rightTrue
    global leftTrue
    #if pressed character is not a special character, save it into variable a
    #this is needed bc key.char gives error for spec characters
    try:
        a = key.char
    except:
        a = 0

    #pressing r start the recording
    if a == 'r':
        print('recording')
        global isRecording
        isRecording = True
        global startTime
        startTime = time.time()
        global lista 
        lista = []

    #pressing e stops the recording
    if a == 'e':
        isRecording = False
        print('recording stopped')
        print(lista)

    #p plays back the recording
    if a == 'p':       
        try:
            repeat = int(input('How many times?\n'))
            for x in range(0, repeat):
                play()
        except:
            play()

    #z plays back the recording reversed
    if a == 'z':
        try:
            repeat = int(input('How many times?\n'))
            for x in range(0, repeat):
                playReverse()
        except:
            playReverse()

    if key == Key.up and forwTrue == False:
        signal = '#FWRD\n'
        write(signal)
        record(signal)
        forwTrue = True
    if key == Key.down and backTrue == False:
        signal = '#BACK\n'
        write(signal)
        record(signal)
        backTrue = True
    if key == Key.left and leftTrue == False:
        signal = '#LEFT\n'
        write(signal)
        record(signal)
        leftTrue = True
    if key == Key.right and rightTrue == False:
        signal = '#RGHT\n'
        write(signal)
        record(signal)
        rightTrue = True

def on_release(key):
    global forwTrue
    global backTrue
    global rightTrue
    global leftTrue

    if key == Key.up:
        signal = '#FWR0\n'
        write(signal)
        record(signal)
        forwTrue = False
    if key == Key.down:
        signal = '#BAC0\n'
        write(signal)
        record(signal)
        backTrue = False
    if key == Key.left:
        signal = '#LEF0\n'
        write(signal)
        record(signal)
        leftTrue = False
    if key == Key.right:
        signal = '#RGH0\n'
        write(signal)
        record(signal)
        rightTrue = False
    if key == Key.esc:
        # Stop listener
        return False


def ControlListener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

#try to open serial port
try:
    ser1 = serial.Serial('COM5', 9600)  # open serial port
    print(ser1.name)         # check which port was really used
    #ser.write('#STAR\n'.encode('utf-16'))     # write a string
    time.sleep(2)
    print('well slept ;) \n')
    _thread.start_new_thread(ControlListener, ())

#if there is no serial port, write out commands
except:
    print('COM5 port is not available \n')
    _thread.start_new_thread(ControlListener, ())

while 1:
   pass