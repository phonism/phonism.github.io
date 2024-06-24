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
    if fl.startswith("photo") and fl.find(".jpg") != -1:
        image = Image.open(fl)

        thumbnail_size = (840, 560)  # 缩略图大小
        image.thumbnail(thumbnail_size)

        slt = "slt_" + fl
        image.save(slt)

        width, height = image.size
        dic = {
                "src": "myworks/" + fl,
                "slt_src": "myworks/" + slt,
                "w": width,
                "h": height,
        }
        js["gallery"].append(dic)

print("var myData = " + json.dumps(js, ensure_ascii=False, indent=4))
