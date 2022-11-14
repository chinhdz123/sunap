from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from loguru import logger
import cv2
import os
import warnings
warnings.filterwarnings("ignore")

cfg = get_cfg()
cfg.merge_from_file("config.yaml")

# Create predictor

logger.info("start_load_md")
predictor = DefaultPredictor(cfg)
logger.info("end_load_md")


# Make prediction
path = r"D:\20223\python\api-ocr1\web_ocr_api\chinh.jpg"

image = cv2.imread(path)
logger.info("start_load_img")
logger.info(path)
output = predictor(image)
boxes = output["instances"].to("cpu").pred_boxes if output["instances"].to("cpu").has("pred_boxes") else None
print(boxes)

