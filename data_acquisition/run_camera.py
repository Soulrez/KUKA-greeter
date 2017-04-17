'''
Captures an image from webcam every N seconds using OpenCV
'''
import time
from cv2 import *

def capture(index, name):
    # Use /dev/video1
    # If using another device, change 1 to device number
    cam = VideoCapture(1)
    s, img = cam.read()
    if s:
        namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("evolvingai/"+name+"/image-"+index+".jpg",img)

if __name__ == '__main__':
    # Name of the person that's getting their photos taken
    name = "richard"
    # Run this for 6 hours
    for i in range(0,21600):
        # Take photo every 60 seconds
        print(i)
        if i%60 == 0:
            capture(str(i/60),name)
        time.sleep(1)
