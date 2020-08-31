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
    
<br>
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
<br>
    - 데이터를 읽어옴<br>
<pre><code>
train = pd.read_csv('root/train.csv')
test = pd.read_csv('root/test.csv')
</code></pre>
    - csv로부터 데이터를 읽고, train_image 폴더와 test_image 폴더에 각각 이미지 저장하기<br>
<pre><code>
def make_folder(directory_path):
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path) 
<br><br>
path_train = os.path.join(os.getcwd(), 'data/emnist/train')
path_val = os.path.join(os.getcwd(), 'data/emnist/val')
path_test = os.path.join(os.getcwd(), 'data/emnist/test')
<br><br>
make_folder(path_train)
make_folder(path_val)
make_folder(path_test)
<br><br>
for i in range(10):
    path_train_digit = os.path.join(path_train, str(i))
    path_val_digit = os.path.join(path_val, str(i))
    make_folder(path_train_digit)
    make_folder(path_val_digit)
<br><br>
for i in range(len(train)):
    digit = train.loc[i, 'digit']
    #print(i)
    letter = train.loc[i, 'letter'] # letter
    img = train.loc[i, '0':].values.reshape(28, 28).astype(int)
<br><br>
    path_train_digit = os.path.join(path_train, str(digit))
    path_val_digit = os.path.join(path_val, str(digit))
    # cv2.imwrite(img, 'save_name')
    if digit == 0:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 1:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 2:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 3:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 4:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 5:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        cv2.imwrite(path_train_image, img)
    elif digit == 6:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 7:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 8:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
    elif digit == 9:
        path_train_image = os.path.join(path_train_digit, '%d_%c.jpg'%(i,letter))
        path_val_image = os.path.join(path_val_digit, '%d_%c.jpg'%(i, letter))
        ran_num = randint(0,4)
        if ran_num ==0:
            cv2.imwrite(path_val_image, img)
        else:
            cv2.imwrite(path_train_image, img)
<br><br>
for i in range(len(test)):
    letter = test.loc[i, 'letter'] # letter
    img = test.loc[i, '0':].values.reshape(28, 28).astype(int)
    path_test_digit = os.path.join(path_test, '%d_%c.jpg'%(i, letter))
    cv2.imwrite(path_test_digit, img)
</code></pre>

<pre><code>
"""
class FaceLandmarksDataset(Dataset):                # 근데 이거 클래스 이름이 왜 이렇지?? Dataset 클래스 아닌가??
    def __init__(self, csv_file, root_dir, transform = None):
        # csv_file (string) : Path to the csv file with annotations
        # root_dir (string) : Directory with all the images
        # transform (callable, optional) : Optional transform to be applied on a sample
    def __len__(self):
        return len(self, landmarks_frame)
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        img_name = os.path.join(self.root_dir, self.landmarks_frame.iloc[idx, 0])
        image = io.imread(img_name)
        landmarks = self.landmarks_frame.iloc[idx, 1:]
        landmarks = np.array([landmarks])
        landmarks = landmarks.astype('float').reshape(-1, 2)
        sample = {'image' = image, 'landmarks' : landmarks}
        if self.transform :
            sample = self.transform(sample)
        return sample
"""
train_dataset = Dataset('/root/train.csv', 'root/train_image', transform = None)
test_dataset = Dataset('/root/test.csv', 'root/test_image', transform = None)

</code></pre>



- dataset 만드는 방법
    1. 폴더구조 사용하기<br> (ex)<br>root/train/dog/blahblah.png<br>/cat/blahblag.png ...
    1. dataset class 를 사용하기<br>__ len__ (self) : (ex)__ len__ (dataset) --> dataset size 반환<br>__ getitem__(self, idx) : idx번째 dataset[idx]의 값을 반환<br>
- transform 을 사용해 image data compose 하기
    <pre><code>
    #예시
    trans = transforms.Compose([transforms.Resize((224,224),transforms.ToTensor(), transforms.Nomarlize((0.4,0.4),(0.39,0.21),(0.142,0.432)))])
    </code></pre>
- ImageFolder 를 사용해 dataload 하기
    <pre><code>
    #예시
    train_data = torchvision.datasets.ImageFolder(root = './dataset/train',transform = trans)
    test_data = torchvision.datasets.ImageFolder(root = './dataset/train',transform = trans)
    </code></pre>
- DataLoader 로 dataset 을 batch image로 불러오기
    <pre><code>
    #예시
    train_set = dataLoader(dataset = train_data, batch_size = 8, shuffle = True, num_workers = 2)
    test_set = dataLoader(dataset = test_data, batch_size = len(test_data))
    </code></pre>
        