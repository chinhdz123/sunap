from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from loguru import logger
import cv2
import os
import warnings
warnings.filterwarnings("ignore")

cfg = get_cfg()
cfg.merge_from_file("output\config.yaml")
# Create predictor

logger.info("start_load_md")
predictor = DefaultPredictor(cfg)
logger.info("end_load_md")
def convert_boxes(boxes):
    return boxes.tensor.numpy()

def find_line_circles(circles):
    a = circles[0][1]
    group_lines = []
    group_line = []
    for i in range(len(circles)):
        if circles[i][1]+4/5*circles[i][2] > a and circles[i][1]-4/5*circles[i][2] < a:
            group_line.append(circles[i])
        else:
            print(group_line)
            group_lines.append(group_line)
            group_line = []
            group_line.append(circles[i])
            a = circles[i][1]
    group_lines.append(group_line)
    return group_lines
# Make prediction
path = "sunap.jpg"

image = cv2.imread(r"data/"+path)
logger.info("start_load_img")
logger.info(path)
output = predictor(image)
boxes = output["instances"].to("cpu").pred_boxes if output["instances"].to("cpu").has("pred_boxes") else None
print(boxes)
if boxes is not None:
    boxes = convert_boxes(boxes)
circles= []
for box in boxes:
    x0, y0, x1, y1 = box
    center_X =  int((x1+x0)/2)
    center_Y = int((y1+y0)/2)
    r = int((x1-x0)/2)
    circles.append([center_X,center_Y,r])
    circles = sorted(circles, key=lambda b: b[1])

group_lines = find_line_circles(circles)
count = 0
x = []
y = []
for group_line in group_lines:
    group_line = sorted(group_line, key=lambda b: b[0])
    for circle in group_line:
        if count>=41 and count != 46 and count != 51 and count != 56 and count != 61:
            cv2.circle(image, (circle[0], circle[1]), circle[2], (0, 255, 0), 1)
            cv2.circle(image, (circle[0], circle[1]), 2, (0, 0, 255), 1)
            cv2.putText(image, str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            x.append(circle[0])
            y.append(circle[1])

        count +=1
print("x",x)
print("y",y)
logger.info("end_load_img")

cv2.imwrite('tmp//'+path, image)