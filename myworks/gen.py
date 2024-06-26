from PIL import Image
from PIL.ExifTags import TAGS
import os
import json
import copy

js = {
    "designer": {
        "name": "Gallery",
        "tag": ["A programmer with a passion for landscape and wildlife photography."],
        "bg": "#222222",
    },
    "recommend":{
        "city": "上海"
    },
    "hawaii": [],
    "birds": [],
    "index": []
}



def update_js(img_path, tag):
    file_list = sorted(os.listdir(img_path))
    for fl in file_list:
        if fl.startswith("DSC_") and fl.find(".jpg") != -1:
            image = Image.open(img_path + "/" + fl)
            #exif_data = image._getexif()
            #for tag, value in exif_data.items():
                #tag_name = TAGS.get(tag, tag)
                #print(tag_name, value)
            width, height = image.size

            thumbnail_size = (840, 560)  # 缩略图大小
            image.thumbnail(thumbnail_size)

            slt = "slt_" + fl
            image.save(img_path + "/" + slt)

            dic = {
                    "src": "../myworks/" + img_path + "/" + fl,
                    "slt_src": "../myworks/" + img_path + "/" + slt,
                    "w": width,
                    "h": height,
            }
            js[tag].append(dic)

update_js("hawaii", "hawaii")
update_js("birds", "birds")

js["index"].append(copy.deepcopy(js["hawaii"][0]))
js["index"][-1]["src"] = js["index"][-1]["src"].split("../")[-1]
js["index"][-1]["slt_src"] = js["index"][-1]["slt_src"].split("../")[-1]
js["index"][-1]["url"] = "html/hawaii.html"
js["index"][-1]["title"] = "Hawaii"

js["index"].append(copy.deepcopy(js["birds"][0]))
js["index"][-1]["src"] = js["index"][-1]["src"].split("../")[-1]
js["index"][-1]["slt_src"] = js["index"][-1]["slt_src"].split("../")[-1]
js["index"][-1]["url"] = "html/birds.html"
js["index"][-1]["title"] = "Birds"

print("var myData = " + json.dumps(js, ensure_ascii=False, indent=4))
