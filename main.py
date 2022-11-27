from loguru import logger
import cv2
import warnings
from control_rb import control
warnings.filterwarnings("ignore")
from utils import *
from datetime import date, datetime
import os
from mypackage.speak_hear import *
from mymodule.talk import *


def gird():
    cap = cv2.VideoCapture(0)
    while True:
        ss, img = cap.read()
        if ss:
            circles = find_total_circles(img)
            print(len(circles))
            x = [circle[0] for circle in circles]
            y = [circle[1] for circle in circles]
            # bước 2: convert vị trí bằng model
            x_robot,y_robot = convert_to_x_y_robot(x,y)
            # bước 3: điều khiển robot theo các vị trí
            control(x_robot,y_robot)
            speak("tôi đã làm xong")
            cv2.imwrite("img.jpg",img)
            cv2.waitKey(10)
            cv2.destroyAllWindows()
            break


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
        speak("ô kê, rô bốt lên nào")
    elif "xuống" in you:
        speak("ô kê, rô bốt xuống nào")





