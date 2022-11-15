from utils import find_circles
import cv2
import json
from sklearn.model_selection import train_test_split
#vị trí 1
label_x = [310,282,254,226,309,283,252,225,310,282,254,226,195,310,283,254,225,197,309,283,254,227,198]
label_y = [-39,-39,-37,-37,-10,-9,-9,-8,19,21,20,20,20,47,48,48,49,51,75,77,76,79,81]

label_x_max = max(label_x)
print(label_x_max)
label_y_max = max(label_y)
print(label_y_max)
label_x= [i/label_x_max for i in label_x]
label_y= [i/label_y_max for i in label_y]



img = cv2.imread(r"data\sunap2.jpg")
x,y = find_circles(img)
print(x, y)
x_max = max(x)
y_max = max(y)
x = [i/x_max for i in x]
y = [i/y_max for i in y]

x_train, x_test, label_x_train, label_x_test = train_test_split(x, label_x, test_size=0.025, random_state=42)
y_train, y_test, label_y_train, label_y_test = train_test_split(y, label_y, test_size=0.025, random_state=42)


# Data to be written
data1 = {
    "x_train": x_train,
    "label_x_train": label_x_train,
    "x_test": x_test,
    "label_x_test": label_x_test,
    "y_train": y_train,
    "label_y_train": label_y_train,
    "y_test": y_test,
    "label_y_test": label_y_test,
}
 
with open("data_json\data.json", "w") as outfile:
    json.dump(data1, outfile)
