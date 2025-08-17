import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Hue,saturation,Value
mycolorHSV = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]
            ]
# BGR Range
myColors =  [[51,153,255],          
            [255,0,255],
            [0,255,0],
            [255,0,0]
            ]

myPoints = []

def findcolor(img,mycolorHSV,myColors):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in mycolorHSV:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv.circle(imgResult,(x,y),15,myColors[count],cv.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count += 1
    return newpoints
        
        
def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoints,myColors):
    for point in myPoints:
        cv.circle(imgResult,(point[0],point[1]),10,myColors[point[2]],cv.FILLED)
        

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findcolor(img,mycolorHSV,myColors)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:\
        drawOnCanvas(myPoints,myColors)
    cv.imshow("Result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break