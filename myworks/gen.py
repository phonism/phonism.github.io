from PIL import Image
from PIL.ExifTags import TAGS
import os
import json

js = {
    "designer": {
        "name": "Gallery",
        "tag": ["A beginner photographer focusing on landscape and bird photography."],
        "bg": "#222222",
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
        #exif_data = image._getexif()
        #for tag, value in exif_data.items():
            #tag_name = TAGS.get(tag, tag)
            #print(tag_name, value)
        width, height = image.size

        thumbnail_size = (840, 560)  # 缩略图大小
        image.thumbnail(thumbnail_size)

        slt = "slt_" + fl
        image.save(slt)

        dic = {
                "src": "myworks/" + fl,
                "slt_src": "myworks/" + slt,
                "w": width,
                "h": height,
        }
        js["gallery"].append(dic)

print("var myData = " + json.dumps(js, ensure_ascii=False, indent=4))
