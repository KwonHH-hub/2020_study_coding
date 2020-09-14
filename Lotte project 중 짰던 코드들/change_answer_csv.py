import csv
import os

dir = os.getcwd()
dir_ = os.path.join(dir, 'answer.csv')
print(dir_)
# 원래 리스트
# list = ['toreta', 'squid_peanut', 'homerunball','cidar','coke',
#          'diget_ori','diget_choco','buttering','zec', 'welchs',
#          'vita500','chocopie','couque_coffee','couque_white','gumi_gumi',
#          'ID_gum','spearmint','juicyfresh','tuna','samdasu',
#          'jjolbyung_ori','jjolbyung_noodle']

# 원래 리스트에 # ['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '3', '4', '5', '6', '7', '8', '9']
# list = ['toreta', 'squid_peanut', 'vita500','chocopie','couque_coffee',
#         'couque_white','gumi_gumi', 'ID_gum','spearmint','juicyfresh',
#         'tuna','samdasu','homerunball','jjolbyung_ori','jjolbyung_noodle',
#         'cidar','coke', 'diget_ori','diget_choco','buttering','zec', 'welchs']

# class 순서에 따른 리스트
# list = ['ID_gum', 'buttering', 'couque_coffee','chocopie','cidar',
#         'couque_white','coke','diget_ori', 'diget_choco','gumi_gumi','homerunball',
#         'jjolbyung_noodle','juicyfresh','jjolbyung_ori','spearmint','squid_peanut',
#         'samdasu','tuna', 'toreta','vita500','welchs','zec']

# class 순서에 따른 리스트 에 ['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '3', '4', '5', '6', '7', '8', '9']
list = ['ID_gum', 'buttering', 'homerunball','jjolbyung_noodle','juicyfresh',
        'jjolbyung_ori','spearmint', 'squid_peanut','samdasu','tuna',
        'toreta','vita500','couque_coffee','welchs','zec',
        'chocopie','cidar', 'couque_white','coke','diget_ori','diget_choco','gumi_gumi']

wr_list = []
with open(dir_,'r') as f:
    reader = csv.reader(f)

    for r in reader:
        id = r[0][r[0].find('_')+1:].split('.')[0]

        if id == list[0]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[1]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[2]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[3]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[4]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[5]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[6]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[7]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[8]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[9]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[10]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[11]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[12]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[13]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[14]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[15]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[16]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[17]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[18]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[19]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[20]:
            label = list.index(id)
            wr_list.append([r[0], label])

        elif id == list[21]:
            label = list.index(id)
            wr_list.append([r[0], label])

print('wr_list', wr_list)
dir = os.getcwd()
dir_ = os.path.join(dir, 'answer2.csv')
print(dir_)

with open(dir_,'w',newline='') as ff:
    wr = csv.writer(ff)
    wr.writerow(['id','label'])
    for w in wr_list:
        wr.writerow([w[0], w[1]])