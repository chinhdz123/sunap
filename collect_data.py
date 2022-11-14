from utils import find_circles
import cv2
import json
from sklearn.model_selection import train_test_split
#vị trí 1
label_x = [185.5,187.3,184.7,213,213,214,212.6,212.2,240.1,240,241.7,241.9,241,269,270,270,270.8,269.3,296.5,295.8,296.4,295.9,298.3]
label_y = [39.2,68.6,9.2,-19.8,7.6,37.8,67.8,-46.2,-46.7,-18.7,10.8,38.8,67.8,-48.2,-18.5,9,39.4,67.4,-48.3,-19.4,9.7,39.4,67.7]
# label_x = [296.3,268.7,241.1,212,296.6,268.6,241.3,211.6,296.6,268.6,241.6,213.7,297.4,270.2,241.8,213.2,297.7,270.4,243.1,213.4,298.8,272.4,241.7,215.3]
# label_y = [-98.7,-98.1,-97.5,-96.1,-70,-68.5,-68.1,-68.4,-40.6,-40.2,-39.5,-39.4,-11.4,-12.2,-11.8,-10.5,15.4,16.8,16.7,18.6,45.5,44.9,46.6,47.4]
label_x_max = max(label_x)
print(label_x_max)
label_y_max = max(label_y)
print(label_y_max)
label_x= [i/label_x_max for i in label_x]
label_y= [i/label_y_max for i in label_y]



img = cv2.imread(r"data\sunap1.jpg")
y,x = find_circles(img)
print(x, y)
x_max = max(x)
y_max = max(y)
x = [i/x_max for i in x]
y = [i/y_max for i in y]

x_train, x_test, label_x_train, label_x_test = train_test_split(x, label_x, test_size=0.25, random_state=42)
y_train, y_test, label_y_train, label_y_test = train_test_split(y, label_y, test_size=0.25, random_state=42)


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
