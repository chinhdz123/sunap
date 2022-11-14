import torch
import torch.nn as nn
import json
with open('data_json\data.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

#pre=processing for x data
y_train = json_object["y_train"]
y_test = json_object["y_test"]
label_y_train = json_object["label_y_train"]
label_y_test = json_object["label_y_test"]

Y_train = []
for item in y_train:
    Y_train.append([item**2,item])
Y_train = torch.tensor(Y_train,dtype=torch.float32)

Y_test = []
for item in y_test:
    Y_test.append([item**2,item])
Y_test = torch.tensor(Y_test,dtype=torch.float32)

label_y_train = torch.tensor(label_y_train,dtype=torch.float32)
label_y_test = torch.tensor(label_y_test,dtype=torch.float32)

label_y_train = label_y_train.view(label_y_train.shape[0], 1)
label_y_test = label_y_test.view(label_y_test.shape[0], 1)

n_samples, n_features = Y_train.shape

# 1) Model
# Linear model f = wx + b
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

# 2) Loss and optimizer
learning_rate = 0.01

criterion = nn.MSELoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate,momentum=0.9)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate,betas=[0.9,0.99])


# 3) Training loop
num_epochs = 30000
best_loss = 100
count = 0
for epoch in range(num_epochs):
    # Forward pass and loss
    label_x_predict_train = model(Y_train)
    loss = criterion(label_x_predict_train, label_y_train)
    
    # Backward pass and update
    loss.backward()
    optimizer.step()

    # zero grad before new step
    optimizer.zero_grad()

    if (epoch+1) % 10 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')
        label_y_predict_test = model(Y_test)
        loss_test = criterion(label_y_predict_test, label_y_test)
        print(f'epoch: {epoch+1}, loss_valid = {loss_test.item():.4f}')
        if loss_test < best_loss:
            best_loss = loss_test
            count = 0
        else:
            count+=1
    if count > 100:
        break

torch.save(model, r"D:\20223\datn\AI\sunap\model\model_y.pth")

predicteds = model(Y_test).detach().numpy()
print([predicted*100 for predicted in predicteds])
print([label_x*100 for label_x in label_y_test])

