import threading as th
import cv2, socket, pickle, struct
from math import sqrt
from imutils.video import VideoStream
import mediapipe as mp
import requests, json, base64

class DeamonCapturing():
    def run(self):
        
        cap = cv2.VideoCapture('istockphoto-502606353-640_adpp_is.mp4')

        detector = PoseDetector()
        
        while True:
            _ , img = cap.read()

            detector.findPose(img)
            coords = detector.getPosition(img)
            detector.notice(coords, img)
            #print(lmlist)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

class PoseDetector():
    def __init__(self, mode= False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5) -> None:
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.cnt = 0
        self.ls = (0,0)

        
        try:
            self.client_socket.connect((self.host_ip, self.port))
        except:
            print('Ops!')


    def findPose(self, img  , draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results =self.pose.process(imgRGB)
         
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        self.mpDraw
        return img

    def getPosition(self, img, draw=True):
        lmlist = []

        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0 , 0), cv2.FILLED)
            x=0
            y=0
            for el in lmlist:
                x += el[1]
                y += el[2]
            coords = (int(x/len(lmlist)), int(y/len(lmlist)))
            cv2.circle(img, coords, 5, (255, 234 , 0), cv2.FILLED)
            
        return coords

    def notice(self, coords, img):
        if self.cnt==0:
            print(coords)
            
            if (abs(coords[0]-self.ls[0]) < 2) and (abs(coords[0]-self.ls[0]) < 2):
                try:
                    _, encimg = cv2.imencode(".png ", img)
                    img_str = encimg.tostring()
                    img_byte = base64.b64encode(img_str).decode("utf-8")
                    url = 'http://127.0.0.1:8000'
                    data = {'data': {
                        'camera': 66546754,
                        'image': img_byte.encode('utf-8')
                    }}
                    r = requests.post(url , json=data)
                    
                except:
                    print('oops')
                self.ls = coords
        if self.cnt<20:
            self.cnt+=1
        if self.cnt==20:
            self.cnt = 0
        

def main():
    x  = DeamonCapturing()
    x.run()
    
if __name__ == "__main__":
    main()