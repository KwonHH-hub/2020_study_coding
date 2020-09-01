# Pytorch로 EMNIST 분류하기
## SpinalNet 사용해보기 (오픈소스 링크 : <a>https://github.com/dipuk0506/SpinalNet/blob/master/MNIST_VGG/EMNIST_digits_VGG_and%20_SpinalVGG.py)
- Work Flow
    1. Dataset 만들기
    1. Transform 사용해 image data compose 하기 (image size 조정, normalize, tensor로 변경 등)
    1. ImageFolder를 이용해 Data Load 하기
    1. DataLoader로 DataSet(Batch image) 불러오기
    1. Neural Network 만들기
    1. Neural Network 의 Input 과 Output Channel 입력
    1. Optimizer, Loss_func 정의
    1. DataLoader 를 epoch 횟수로 훈련하기
    1. Test 하기<br>자료 참고 : <a>https://blog.naver.com/reisei11/221733757476
<br><br><br>
1. Dataset 만들기
<pre><code>
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import torch
from torchvision import datasets, models, transforms
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import cv2
import os
from random import *
import time
import copy
</code></pre>
- 데이터를 읽어옴<br>
<pre><code>
train = pd.read_csv('root/train.csv')
test = pd.read_csv('root/test.csv')
</code></pre>
- 처음 20개의 데이터 출력해보기
<pre><code>
train.head(20)
</code></pre>
- 읽어들인 데이터로부터 숫자와 알파벳의 종류 확인
<pre><code>
train_digit = train['digit'].values
train_letter = train['letter'].values
print('digit  : ', np.unique(train_digit))
print('letter : ', np.unique(train_letter))
</code></pre>
- 각 digit의 숫자 세기
<pre><code>
train_length = len(train)<br><br>
digit_list = [0 for i in range(np.unique(train_digit))]<br><br>
for i in range(train_length):
    digit = train.loc[i, 'digit']
    if digit==0: digit_list[0] += 1
    elif digit ==1: digit_list[1] += 1
    elif digit ==2: digit_list[2] += 1
    elif digit ==3: digit_list[3] += 1
    elif digit ==4: digit_list[4] += 1
    elif digit ==5: digit_list[5] += 1
    elif digit ==6: digit_list[6] += 1
    elif digit ==7: digit_list[7] += 1
    elif digit ==8: digit_list[8] += 1
    elif digit ==9: digit_list[9] += 1
print(digit_list)
</code></pre>
- train data에 대해서 0~9까지 각각 나누어 폴더에 넣고, test data는 test/emist 경로에 저장
<code><pre>
def make_folder(directory_path):
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)<br><br>
path_train = os.path.join(os.getcwd(), '/train')
""" path_val = os.path.join(os.getcwd(), '/val') """
path_test_prev = os.path.join(os.getcwd(), '/test')
path_test = os.path.join(os.getcwd(), '/test/emnist')<br><br>
make_folder(path_train)  # train 데이터 폴더 생성
""" make_folder(path_val)   # val 데이터 폴더 생성 """
make_folder(path_test_prev)  # test 데이터 폴더 생성
make_folder(path_test)  # test 데이터 폴더 생성<br><br>
for i in range(10):
    path_train_digit = os.path.join(path_train, str(i))  # path_train = /content/train
    """ path_val_digit = os.path.join(path_val, str(i)) """
    make_folder(path_train_digit)  # train 폴더에 0~9 digit 폴더 생성
    """ make_folder(path_val_digit)   # val 폴더에 0~9 digit 폴더 생성 """<br><br>
for i in range(len(train)):  # train 데이터 수만큼 반복
    digit = train.loc[i, 'digit']  """ digit 에 i번째 train 데이터의 숫자 값 넣음 """ <br><br>
    letter = train.loc[i, 'letter']  # letter 에 i번째 train 데이터의 letter 문자 값 넣음
    img = train.loc[i, '0':].values.reshape(28, 28).astype(int)  """ img 에 train 의 i번째 train 데이터의 값을 28 x 28 int 형태로 저장 """<br><br>
    path_train_digit = os.path.join(path_train, str(digit))
    """ path_val_digit = os.path.join(path_val, str(digit)) """<br><br>
    if digit == 0:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 1:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 2:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 3:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 4:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 5:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 6:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 7:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 8:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
    elif digit == 9:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg' % (i, letter))
        # path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        # ran_num = randint(0,4)
        # if ran_num ==0:
        #     cv2.imwrite(path_val_image, img)
        # else:
        #     cv2.imwrite(path_train_image, img)
        cv2.imwrite(path_train_image, img)
</code></pre><br><br>
1. 데이터셋 만들기
    1. Transform 사용해 image data compose 하기 (image size 조정, normalize, tensor로 변경 등)
    1. ImageFolder를 이용해 Data Load 하기
    1. DataLoader로 DataSet(Batch image) 불러오기<br>
<pre><code>
for i in range(len(test)):
    letter = test.loc[i, 'letter'] # letter
    img = test.loc[i, '0':].values.reshape(28, 28).astype(int)
    path_test_digit = os.path.join(path_test, '%d_%c.jpg'%(i, letter))
    cv2.imwrite(path_test_digit, img)<br><br>
    import math
    import torch.nn.functional as F
    import numpy as np<br><br>
    num_epochs = 200
    batch_size_train = 100
    batch_size_test = 1000
    learning_rate = 0.005
    momentum = 0.5
    log_interval = 500
    img_size = 28<br>
    trans_train = transforms.Compose(
        [transforms.Grayscale(num_output_channels=1), transforms.Resize(img_size, img_size),
         transforms.RandomPerspective(), transforms.RandomRotation(10, fill=(0)), transforms.ToTensor(),
         torchvision.transforms.Normalize((0.1307,), (0.3081,))])
    trans_test = transforms.Compose(
        [transforms.Grayscale(num_output_channels=1), transforms.Resize(img_size, img_size), transforms.ToTensor(),
         transforms.Normalize((0.1307,), (0.3081,))])<br><br>
    train_data = datasets.ImageFolder(root=path_train, transform=trans_train)
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size_train, shuffle=True)<br><br>
    test_data = datasets.ImageFolder(root=path_test_prev, transform=trans_test)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size_test, shuffle=True)<br><br>
    examples = enumerate(test_loader)
    batch_idx, (example_data, example_targets) = next(examples)
    print(example_data.shape)
</code></pre>    
- 랜덤 샘플 데이터 출력해보기
<pre><code>
import matplotlib.pyplot as plt<br><br>
fig = plt.figure()
for i in range(6):
  plt.subplot(2,3,i+1)
  plt.tight_layout()
  plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
  plt.title("Ground Truth: {}".format(example_targets[i]))
  plt.xticks([])
  plt.yticks([])
fig
</code></pre>
1. Neural Network 만들기
<pre><code>
import torch
import torchvision
import torch.nn as nn
import math
import torch.nn.functional as F
import numpy as np<br><br>
Half_width = 128
layer_width = 128<br><br>
class SpinalVGG(nn.Module):
    def two_conv_pool(self, in_channels, f1, f2):
        s = nn.Sequential(
            nn.Conv2d(in_channels, f1, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(f1),
            nn.ReLU(inplace=True),
            nn.Conv2d(f1, f2, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(f2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        for m in s.children():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
        return s<br><br>
    def three_conv_pool(self, in_channels, f1, f2, f3):
        s = nn.Sequential(
            nn.Conv2d(in_channels, f1, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(f1),
            nn.ReLU(inplace=True),
            nn.Conv2d(f1, f2, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(f2),
            nn.ReLU(inplace=True),
            nn.Conv2d(f2, f3, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(f3),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        for m in s.children():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
        return s<br><br>
    def __init__(self, num_classes=10):
        super(SpinalVGG, self).__init__()
        self.l1 = self.two_conv_pool(1, 64, 64)
        self.l2 = self.two_conv_pool(64, 128, 128)
        self.l3 = self.three_conv_pool(128, 256, 256, 256)
        self.l4 = self.three_conv_pool(256, 256, 256, 256)<br><br>
        self.fc_spinal_layer1 = nn.Sequential(
            nn.Dropout(p=0.5), nn.Linear(Half_width, layer_width),
            nn.BatchNorm1d(layer_width), nn.ReLU(inplace=True), )
        self.fc_spinal_layer2 = nn.Sequential(
            nn.Dropout(p=0.5), nn.Linear(Half_width + layer_width, layer_width),
            nn.BatchNorm1d(layer_width), nn.ReLU(inplace=True), )
        self.fc_spinal_layer3 = nn.Sequential(
            nn.Dropout(p=0.5), nn.Linear(Half_width + layer_width, layer_width),
            nn.BatchNorm1d(layer_width), nn.ReLU(inplace=True), )
        self.fc_spinal_layer4 = nn.Sequential(
            nn.Dropout(p=0.5), nn.Linear(Half_width + layer_width, layer_width),
            nn.BatchNorm1d(layer_width), nn.ReLU(inplace=True), )
        self.fc_out = nn.Sequential(
            nn.Dropout(p=0.5), nn.Linear(layer_width * 4, num_classes), )<br><br>
    def forward(self, x):
        x = self.l1(x)
        x = self.l2(x)
        x = self.l3(x)
        x = self.l4(x)
        x = x.view(x.size(0), -1)<br><br>
        x1 = self.fc_spinal_layer1(x[:, 0:Half_width])
        x2 = self.fc_spinal_layer2(torch.cat([x[:, Half_width:2 * Half_width], x1], dim=1))
        x3 = self.fc_spinal_layer3(torch.cat([x[:, 0:Half_width], x2], dim=1))
        x4 = self.fc_spinal_layer4(torch.cat([x[:, Half_width:2 * Half_width], x3], dim=1))<br><br>
        x = torch.cat([x1, x2], dim=1)
        x = torch.cat([x, x3], dim=1)
        x = torch.cat([x, x4], dim=1)<br><br>
        x = self.fc_out(x)<br><br>
        return F.log_softmax(x, dim=1)
</code></pre>
1. NN train 및 test
<pre><code>
device = 'cuda'
   
# For updating learning rate
def update_lr(optimizer, lr):   
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

# Train the model
total_step = len(train_loader)
curr_lr1 = learning_rate

curr_lr2 = learning_rate

 

model2 = SpinalVGG().to(device)

 

""" Loss and optimizer """
criterion = nn.CrossEntropyLoss()
#optimizer1 = torch.optim.Adam(model1.parameters(), lr=learning_rate)
optimizer2 = torch.optim.Adam(model2.parameters(), lr=learning_rate)
 
""" Train the model """
total_step = len(train_loader)
best_accuracy2 =0

for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model2(images)
        loss2 = criterion(outputs, labels)

        # Backward and optimize
        optimizer2.zero_grad()
        loss2.backward()
        optimizer2.step()

        if i == 499:
            print ("Ordinary Epoch [{}/{}], Step [{}/{}] Loss: {:.4f}"
                   .format(epoch+1, num_epochs, i+1, total_step, loss1.item()))
            print ("Spinal Epoch [{}/{}], Step [{}/{}] Loss: {:.4f}"
                   .format(epoch+1, num_epochs, i+1, total_step, loss2.item()))


       
""" Test the model """
    model2.eval()
    with torch.no_grad():
        correct2 = 0
        total2 = 0
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
           
            outputs = model2(images)
            _, predicted = torch.max(outputs.data, 1)
            total2 += labels.size(0)
            correct2 += (predicted == labels).sum().item()
   
        if best_accuracy2>= correct2 / total2:
            curr_lr2 = learning_rate*np.asscalar(pow(np.random.rand(1),3))
            update_lr(optimizer2, curr_lr2)
            print('Test Accuracy of SpinalNet: {} % Best: {} %'.format(100 * correct2 / total2, 100*best_accuracy2))
        else:
            best_accuracy2 = correct2 / total2
            net_opt2 = model2
            print('Test Accuracy of SpinalNet: {} % (improvement)'.format(100 * correct2 / total2))


        model2.train()
</code></pre>