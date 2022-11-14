from loguru import logger
import cv2
import warnings
from control_robot.control_rb import control
warnings.filterwarnings("ignore")
from utils import *


img = cv2.imread(r"tmp\sunap.jpg")
# bước 1: tìm vị trí sunap trên ảnh
x,y = find_circles(img)
# bước 2: convert vị trí bằng model
# x = [ 519, 644, 775, 908, 511, 644, 779, 922, 507, 644, 785, 932, 499, 643, 793, 947, 486, 639, 799, 964, 476, 635, 804, 980]
# y = [ 993, 988, 980, 965, 1107, 1101, 1095, 1081, 1231, 1230, 1221, 1209, 1367, 1364, 1357, 1349, 1513, 1510, 1505, 1502, 1671, 1673, 1674, 1676]
x_robot,y_robot = convert_to_x_y_robot(x,y)

print("x_robot",x_robot)
print("y_robot",y_robot)
# bước 3: điều khiển robot theo các vị trí
control(x_robot,y_robot)

