import math
import torch
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from loguru import logger
import cv2
import warnings
from control_robot import control
warnings.filterwarnings("ignore")
cfg = get_cfg()
cfg.merge_from_file("output\config.yaml")
logger.info("start_load_md")
predictor_circles = DefaultPredictor(cfg)
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
            group_lines.append(group_line)
            group_line = []
            group_line.append(circles[i])
            a = circles[i][1]
    group_lines.append(group_line)
    return group_lines

def find_circles(img):
    output = predictor_circles(img)
    boxes = output["instances"].to("cpu").pred_boxes if output["instances"].to("cpu").has("pred_boxes") else None
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
            if count>41 and count != 46 and count != 51 and count != 56 and count != 61:
                cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 255, 0), 1)
                cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 1)
                cv2.putText(img, str(count), (circle[0], circle[1]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                x.append(circle[0])
                y.append(circle[1])
            count +=1
    return x, y
def convert_to_x_y_robot(x,y):
    model_x = torch.load(r"model\model_x.pth")
    model_y = torch.load(r"model\model_y.pth")
    X = []
    x = [i/1000 for i in x]
    for item in x:
        X.append([item**2,item])
    X = torch.tensor(X,dtype=torch.float32)
    
    predicteds_X = model_x(X).detach().numpy()
    predicteds_X = [math.floor(predicted_X.item()*300) for predicted_X in predicteds_X]

    y = [i/1700 for i in y]
    Y = []
    for item in y:
        Y.append([item**2,item])
    Y = torch.tensor(Y,dtype=torch.float32)

    predicteds_Y = model_y(Y).detach().numpy()
    predicteds_Y = [math.floor(predicted_Y.item()*100) for predicted_Y in predicteds_Y]

    return predicteds_X,predicteds_Y