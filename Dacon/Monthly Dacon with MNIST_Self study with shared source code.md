# VGG-19 (spinal FC) 오픈소스 공부
## 출처 : https://github.com/dipuk0506/SpinalNet

import torch
import torchvision
import torch.nn as nn
import math
import torch.nn.functional as F
import numpy as np

num_epochs = 200
batch_size_train = 100
batch_size_test = 1000
learning_rate = 0.005
momentum = 0.5
log_interval = 500


<pre>
<code>
train_loader = torch.utils.data.DataLoader(
  torchvision.datasets.EMNIST('/files/', split='digits', train=True, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.RandomPerspective(), 
                               torchvision.transforms.RandomRotation(10, fill=(0,)), 
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=batch_size_train, shuffle=True)
</code>
</pre>
- Dataset 클래스
    - torch.utils.data.Dataset 은 데이터셋을 타나내는 추상클래스
        - Transfrom
            1. Rescale : 이미지의 크기를 조절
            1. RndomCrop : 이미지를 무작위로 자름<br>==> 이것들을 Data Augmentation이라고 함
        - Compose Transform
    


test_loader = torch.utils.data.DataLoader(
  torchvision.datasets.EMNIST('/files/', split='digits', train=False, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=batch_size_test, shuffle=True)

examples = enumerate(test_loader)
batch_idx, (example_data, example_targets) = next(examples)


print(example_data.shape)

