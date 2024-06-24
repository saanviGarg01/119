import cv2
import time
import math


video = cv2.VideoCapture("footvolleyball.mp4")
#load tracker 
tracker = cv2.TrackerCSRT_create()

#read the first frame of the video
success,img = video.read()

#selct the bounding box on the image
bbox = cv2.selectROI("tracking",img,False)

#initialise the tracker on the img and the bounding box
tracker.init(img,bbox)



   
def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
   check,img = video.read()
   success,bbox = tracker.update(img)
   
   #Write the code inside loop here
   if success:
       drawBox(img,bbox)
   else :
       cv2.putText(img,"lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

video.release()
cv2.destroyALLwindows() 