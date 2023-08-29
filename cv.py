import cv2
from cvzone.ClassificationModule import Classifier
import serial 

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(5, 80)
cap.set(10, 0)
cls = Classifier("model","labels")
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1) 
def run():
    _, img = cap.read()
    if cls.getPrediction(img)[1]==1:
        arduino.write(bytes(1,  'utf-8'))
    else:
        arduino.write(bytes(0,  'utf-8'))

    cv2.waitKey(1)