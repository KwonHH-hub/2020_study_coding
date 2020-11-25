import os
import xml.etree.ElementTree as elt
from PIL import Image
import random


def int2str(num):
    if num >= 0 and num <= 9:
        return '000' + str(num)
    elif num >= 10 and num <= 99:
        return '00' + str(num)
    elif num >= 100 and num < 999:
        return '0' + str(num)
    else:
        return str(num)


xml_path_list = [
    r'C:\Users\사용자\Desktop\pascal_voc\pascalVOC_hh\Annotations',
    r'C:\Users\사용자\Desktop\pascal_voc\pascalVOC_ih\Annotations',
    r'C:\Users\사용자\Desktop\pascal_voc\pascalVOC_jw\Annotations',
    r'C:\Users\사용자\Desktop\pascal_voc\pascalVOC_mh\Annotations'
]
file_dict = {}
number = 0

save_Dir = 'C:/Users/사용자/Desktop/New200930/Annotations/'
img_save_Dir = 'C:/Users/사용자/Desktop/New200930/JPEGImages/'

for xpl in xml_path_list:
    xml_name_list = os.listdir(xpl)
    print(xml_name_list)

    for n in xml_name_list:
        file_dict[n] = number
        number += 1
        xml_file = xpl + '\\' + n

        tree = elt.parse(xml_file)
        root = tree.getroot()

        num = file_dict[n]
        target_file_name = root.find("filename")
        original_name = target_file_name.text
        modified_name = original_name.replace(original_name.split('.')[0], int2str(num))
        target_file_name.text = modified_name

        target_path = root.find("path")
        modified_path = 'PascalVoc/Annotations' + int2str(num) + '.jpg'
        target_path.text = modified_path

        img_targetDir = xpl.replace('Annotations', 'JPEGImages')
        img_path = img_targetDir + '\\' + n.split('.')[0] + '.jpg'

        im = Image.open(img_path)

        TrTest_select = random.randint(1, 10)
        if TrTest_select > 7:
            save_path = save_Dir + 'test2017/' + int2str(num) + '.xml'
            tree.write(save_path)

            img_save_path = img_save_Dir + 'test2017/' + int2str(num) + '.jpg'
            im.save(img_save_path)
        else:
            TrVal_select = random.randint(1, 4)
            if TrVal_select == 1:
                save_path = save_Dir + 'val2017/' + int2str(num) + '.xml'
                tree.write(save_path)

                img_save_path = img_save_Dir + 'val2017/' + int2str(num) + '.jpg'
                im.save(img_save_path)

            else:
                save_path = save_Dir + 'train2017/' + int2str(num) + '.xml'
                tree.write(save_path)

                img_save_path = img_save_Dir + 'train2017/' + int2str(num) + '.jpg'
                im.save(img_save_path)

print(file_dict)
print("finish")