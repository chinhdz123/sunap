#bước 1: thu thập data
# x [ 519, 644, 775, 908, 511, 644, 779, 922, 507, 644, 785, 932, 499, 643, 793, 947, 486, 639, 799, 964, 476, 635, 804, 980]
# y [ 993, 988, 980, 965, 1107, 1101, 1095, 1081, 1231, 1230, 1221, 1209, 1367, 1364, 1357, 1349, 1513, 1510, 1505, 1502, 1671, 1673, 1674, 1676]
# x_thuc [296.3,268.7,241.1,212,296.6,268.6,241.3,211.6,296.6,268.6,241.6,213.7,297.4,270.2,241.8,213.2,297.7,270.4,243.1,213.4,298.8,272.4,241.7,215.3]
# y_thuc [-98.7,-98.1,-97.5,-96.1,-70,-68.5,-68.1,-68.4,-40.6,-40.2,-39.5,-39.4,-11.4,-12.2,-11.8,-10.5,15.4,16.8,16.7,18.6,45.5,44.9,46.6,47.4]
#bước 2: xác định model
#bước 3: tính gradient loss, tìm para
#bước 4: predict
#bước 5: chuyền cho robot
""" import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

x = [ 519, 644, 775, 908, 511, 644, 779, 922, 507, 644, 785, 932, 499, 643, 793, 947, 486, 639, 799, 964, 476, 635, 804]

X = []
for item in x:
    X.append([item**2,item])
X = torch.tensor(X,dtype=torch.float32)
x_sps, X_features = X.shape
print(x_sps, X_features)
# y = np.array([ 993, 988, 980, 965, 1107, 1101, 1095, 1081, 1231, 1230, 1221, 1209, 1367, 1364, 1357, 1349, 1513, 1510, 1505, 1502, 1671, 1673, 1674, 1676])
x_r = torch.tensor([296.3,268.7,241.1,212,296.6,268.6,241.3,211.6,296.6,268.6,241.6,213.7,297.4,270.2,241.8,213.2,297.7,270.4,243.1,213.4,298.8,272.4,241.7],dtype=torch.float32)
model = nn.Linear(2,1)
ln_r = 0.001
iters = 4

loss = nn.MSELoss()
optimize = torch.optim.SGD(model.parameters(),lr = ln_r)

for epoch in range(iters):
    x_pred = model(X)
    l = loss(x_r,x_pred)
    l.backward()
    optimize.step()
    optimize.zero_grad()
    print("loss",l)
X_test = torch.tensor([980],dtype=torch.float32)
print(model(X_test).item())
 """
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
        img = image.GetArray()
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)
        cv2.imshow('title', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()