import xml.etree.ElementTree as et
import json
import os
from collections import OrderedDict

xml_dir_list = [
    r'C:\Users\사용자\Desktop\New200930\Annotations\train2017',
    r'C:\Users\사용자\Desktop\New200930\Annotations\val2017',
    r'C:\Users\사용자\Desktop\New200930\Annotations\test2017'
]
total_dict = {}
total_list = []

key_list = ["folder", "filename", "path", "source", "size", "segmented", "object"]
file_data = OrderedDict()

for xdl in xml_dir_list:
    xml_in_file = os.listdir(xdl)
    for xif in xml_in_file:
        xml_file = et.parse(xdl + '/' + xif)
        root = xml_file.getroot()
        # et.dump(xml_file)

        json_dict = {}
        # json_dict['@verified'] = 'yes'
        current_dict = {}
        object_list = []

        attrib_list = ['source', 'size', 'object']

        for s in root:
            if s.tag in attrib_list:
                if s.tag == 'object':
                    for oo in s.iter():
                        if oo.text.split(' ')[0] == '\n':
                            continue
                        current_dict[oo.tag] = oo.text
                    object_list.append(current_dict)

                else:
                    for ss in s.iter():
                        if ss.text.split(' ')[0] == '\n':
                            continue
                        current_dict[ss.tag] = ss.text
                    json_dict[s.tag] = current_dict
                    current_dict = {}
            else:
                json_dict[s.tag] = s.text
        json_dict['object'] = object_list
        total_list.append(json_dict)
        # print(json_dict)



    # for tl in total_list:
    #     for k in key_list:
    #         file_data[k] = tl[k]
    file_data['images'] = total_list
    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

    with open(xdl + '.json', 'w') as jf:
        json.dump(file_data, jf, ensure_ascii=False, indent="\t")















































# xml_dir = '/content/drive/My Drive/0000.xml'
# xml_file = et.parse(xml_dir)
# root = xml_file.getroot()
#
# et.dump(xml_file)
#
# json_dict = {}
# # json_dict['@verified'] = 'yes'
# current_dict = {}
# object_list = []
#
# attrib_list = ['source', 'size', 'object']
#
# for s in root:
#     if s.tag in attrib_list:
#         if s.tag == 'object':
#             for oo in s.iter():
#                 if oo.text.split(' ')[0] == '\n':
#                     continue
#                 current_dict[oo.tag] = oo.text
#             object_list.append(current_dict)
#
#
#         else:
#             for ss in s.iter():
#                 # print('ss', ss.text)
#                 if ss.text.split(' ')[0] == '\n':
#                     continue
#                 current_dict[ss.tag] = ss.text
#             json_dict[s.tag] = current_dict
#             current_dict = {}
#     else:
#         json_dict[s.tag] = s.text
#     json_dict['object'] = object_list
#
# print(json_dict)
#
# key_list = ["folder", "filename", "path", "source", "size", "segmented", "object"]
# file_data = OrderedDict()
#
# for k in key_list:
#   file_data[k] = json_dict[k]
#
# print(json.dumps(file_data, ensure_ascii=False, indent = "\t"))
#
# with open('/content/drive/My Drive/0000.json','w') as jf:
#   json.dump(file_data,jf,ensure_ascii=False, indent="\t")