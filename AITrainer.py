import cv2
import mediapipe as mp
import time
import numpy as np
import PoseModule as pm

#Created cap and gets the video capture
cap = cv2.VideoCapture(0)
#Gets the dectector using PoseModule
detector = pm.poseDetector(detectioncon=0.7)
count = 0
direction =0
#These landmarks are for the shoulders
tipIDs = [8,12]

start = False
color = (255, 0, 255)
while True:
    #Reads capture and finds pose
    success, img = cap.read()
    img = detector.findPose(img)

    lmList = detector.findPosition(img, draw= False)

#When arms are above shoulders start counting
    if len(lmList) != 0 :
        if lmList[20][2] < lmList[12][2] & lmList[19][2] < lmList[11][2]:
            start = True
            print("worked")


#startings counting and detects when the angle of the armpits reach certain values
    #print(lmList)
    if len(lmList) != 0 :
        if(start == True):
            detector.findAngle(img, 14,12,24 )
            angle = detector.findAngle(img, 13, 11, 23)
            percent = np.interp(angle,(70,150), (0,100))
            bar  = np.interp(angle,(70,150), (120,650))
            #print(percent)


            if percent == 0:
                if direction ==0:
                    color = (255, 0, 255)
                    count += 1
                    direction = 1
                    print(count)
            if percent == 100:
                if direction ==1:
                    color = (0, 255, 0)
                    direction = 0

#Draw a progress bar and counter on img
            cv2.putText(img, str(count), (0, 120), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 5)
            cv2.rectangle(img, (0, 120), (150, 720), color,3)
            cv2.rectangle(img, (0,int(bar)),(150,720),color, cv2.FILLED)






    cv2.imshow("Image",img)
    cv2.waitKey(1)