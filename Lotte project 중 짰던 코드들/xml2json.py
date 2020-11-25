import xml.etree.ElementTree as et
import json
import os
from collections import OrderedDict

xml_dir_list = [
    r'C:\Users\사용자\Desktop\New200930\Annotations\train2017',
    r'C:\Users\사용자\Desktop\New200930\Annotations\val2017',
    r'C:\Users\사용자\Desktop\New200930\Annotations\test2017'
]

total_list = []

# key_list = ["folder", "filename", "path", "source", "size", "segmented", "object"]
key_list = ["filename", "size", "object"]
file_data = OrderedDict()

for xdl in xml_dir_list:
    xml_in_file = os.listdir(xdl)
    for xif in xml_in_file:
        xml_file = et.parse(xdl + '/' + xif)
        root = xml_file.getroot()
        # et.dump(xml_file)

        json_dict = {}
        current_dict = {}
        relate_dict = {}
        object_list = []

        for r in root:
            if r.tag == 'object':
                for o in r:
                    if o.tag == 'bndbox':
                        for b in o:
                            if b.text.split(' ')[0] == '\n':
                                continue
                            relate_dict[b.tag] = b.text
                            if b.tag == 'ymax':
                                current_dict[o.tag] = relate_dict
                                relate_dict = {}
                                object_list.append(current_dict)
                                current_dict = {}
                    else:
                        if o.text.split(' ')[0] == '\n':
                            continue
                        current_dict[o.tag] = o.text
            elif r.tag == 'source' or r.tag == 'size':
                for s in r:
                    if s.text.split(' ')[0] == '\n':
                        continue
                    json_dict[r.tag] = s.text
            else:
                json_dict[r.tag] = r.text

        json_dict['object'] = object_list
        # print(json_dict)
        total_list.append(json_dict)
        # print(total_list)



    for tl in total_list :
        for k in key_list:
            file_data[k] = tl[k]
    file_data['images'] = total_list
    print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

    with open(xdl + '.json', 'w') as jf:
        json.dump(file_data, jf, ensure_ascii=False, indent="\t")
    file_data = {}


print("finish")
