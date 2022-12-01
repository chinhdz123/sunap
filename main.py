from loguru import logger
import cv2
import warnings
from control_rb import Control_robot
warnings.filterwarnings("ignore")
from utils import *
from datetime import date, datetime
import os
from mypackage.speak_hear import *
from mymodule.talk import *

from pypylon import pylon
import cv2

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned


while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img_cam = image.GetArray()
            cv2.namedWindow('title', cv2.WINDOW_NORMAL)
            cv2.imshow('title', img_cam)
            cv2.imwrite("img1.jpg",img_cam)
            cv2.waitKey(10)
            break
        grabResult.Release()
camera.StopGrabbing()
cv2.destroyAllWindows()

def gird():
    img = cv2.imread('D:\Robot\Sunap\datn\sunap\img1.jpg')
    circles = find_total_circles(img)
    print(len(circles))
    x = [circle[0] for circle in circles]
    y = [circle[1] for circle in circles]
    # bước 2: convert vị trí bằng model
    x_robot,y_robot = convert_to_x_y_robot(x,y)
    # bước 3: điều khiển robot theo các vị trí
    control.main()
    speak("tôi đã làm xong")
    cv2.imwrite("img.jpg",img)
gird()

control =  Control_robot()

while True:

    you = hear()
    
    if you is None:
        speak("Tôi không nghe rõ, bạn có thể nói lại được không")
    elif "tạm biệt" in you:
        speak("tạm biệt")
        exit()
    elif "bắt đầu" in you:
        speak("ô kê, rô bốt sẽ bắt đầu trong ít giây")
        gird()
    elif "dừng" in you:
        speak("ô kê, rô bốt đã dừng lại")
    elif "lên" in you:
        control.up()
        speak("ô kê, rô bốt lên nào")
        
    # elif "xuống" in you:
    #     speak("ô kê, rô bốt xuống nào") 
    # elif "trái" in you:
    #     speak("ô kê, rô bốt lên nào")
    #     control.
    # elif "phải" in you:
    #     speak("ô kê, rô bốt lên nào")
    #     control('right')




