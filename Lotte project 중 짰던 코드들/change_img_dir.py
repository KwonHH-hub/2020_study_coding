from PIL import Image
import os

# 현재 작업 위치
cwd = os.getcwd()
# 이미지 파일이 저장된 폴더 위치
file_dir = os.path.join(cwd, 'test')
# file_dir 내에 있는 이미지 파일들의 리스트
file_list = os.listdir(file_dir)
# 물품 리스트
product_list = ['ID_gum', 'buttering', 'couque_coffee','chocopie','cidar',
        'couque_white','coke','diget_ori', 'diget_choco','gumi_gumi','homerunball',
        'jjolbyung_noodle','juicyfresh','jjolbyung_ori','spearmint','squid_peanut',
        'samdasu','tuna', 'toreta','vita500','welchs','zec']

# 해당 경로에 폴더 생성하기
# for i in range(22):
#     pth = os.path.join(file_dir, str(i))
#     print(pth)
#     os.mkdir(pth)

# 위에서 만든 폴더와 이미지 파일이 함께 있기 때문에 확장자를 확인하고, 이미지 파일인 경우에만 아래의 코드 실행
# 위 인덱스에 해당하는 폴더 번호에 해당 파일의 사진을 넣음
for f in file_list:
    if f[-3:] == 'jpg':

        file_name = os.path.join(file_dir, f)
        # print(file_name)
        im = Image.open(file_name)
        product = f[f.find('_')+1:-4]

        index = product_list.index(product)
        pth = os.path.join(file_dir, str(index))
        # print('file_dir', file_dir)
        # print(os.path.join(pth, f))
        im.save(os.path.join(pth, f), 'JPEG')
