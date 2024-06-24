from PIL import Image
import os
import json

js = {
    "designer": {
        "name": "LuckyQueen's Photo Gallery",
        "tag": [],
        "bg": "#ADD8E6"
    },
    "recommend":{
        "city": "上海"
    },
    "gallery": []
}


file_list = sorted(os.listdir("./"))

for fl in file_list:
    if fl.find(".jpg") != -1:
        image = Image.open(fl)
        width, height = image.size
        dic = {
                "src": "myworks/" + fl,
                "w": width,
                "h": height,
        }
        js["gallery"].append(dic)

print("var myData = " + json.dumps(js, ensure_ascii=False, indent=4))
