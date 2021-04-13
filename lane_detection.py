import cv2
import numpy as np

while 1:
    img = cv2.imread('C:\\Users\\Denni\\Desktop\\1200px-Road_in_Norway.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edge = cv2.Canny(blur,50,150,apertureSize=3)
    height = edge.shape[0]
    polygons = np.array([[(0,height),(1390,height),(710,350)]])
    mask = np.zeros_like(edge)
    p = cv2.fillPoly(mask, polygons ,255)
    masked_image = cv2.bitwise_and(edge , mask)
    lines = cv2.HoughLinesP(masked_image,1,np.pi/180,0,0,0)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imshow('window',img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
