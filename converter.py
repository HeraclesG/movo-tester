import json
from cryptography.fernet import Fernet
import shutil
import os
import json
def update_json(obj1, obj2):
    
    for key, value in obj2.items():
        if key in obj1 and isinstance(obj1[key], dict) and isinstance(value, dict):
            update_json(obj1[key], value)
        else:
            obj1[key] = value

def update_object(obj1, obj2):
    ret = {}
    keys = []
    values = []
    for key, value in obj2.items():
        keys.append(key)
    for key, value in obj1.items():
        values.append(value)
    for i in range(0, len(keys)):
        ret[keys[i]] = values[i]
    return ret

def update_object_add(obj1, obj2):
    ret = {}
    keys = []
    values = []
    for key, value in obj2.items():
        if not key in obj1:
            obj1[key] = value
    return obj1



def convert(src, dist):
    with open((src), 'r', encoding='utf-8') as file_src:
        src_pack = json.load(file_src)
    with open((dist), 'r', encoding='utf-8') as file_dist:
        dist_pack = json.load(file_dist)

    load_pack = update_object(dist_pack, src_pack)
    with open(dist, 'w', encoding='utf-8') as file:
        json.dump(load_pack, file, indent=4, separators=(',', ': '), ensure_ascii=False)
        file.close()

def convert_add(src, dist):
    with open((src), 'r', encoding='utf-8') as file_src:
        src_pack = json.load(file_src)
    with open((dist), 'r', encoding='utf-8') as file_dist:
        dist_pack = json.load(file_dist)

    load_pack = update_object_add(dist_pack, src_pack)
    with open(dist, 'w', encoding='utf-8') as file:
        json.dump(load_pack, file, indent=4, separators=(',', ': '), ensure_ascii=False)
        file.close()
convert("en-US.json", "fr-FR.json")
convert("en-US.json", "de-DE.json")
convert("en-US.json", "es-ES.json")
convert("en-US.json", "pt-PT.json")
convert("en-US.json", "it-IT.json")
convert("en-US.json", "ar-SA.json")
