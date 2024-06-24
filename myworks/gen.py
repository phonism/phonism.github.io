from PIL import Image
import os

for fl in os.listdir("./"):
    if fl.find(".jpg") != -1:
        image = Image.open(fl)
        width, height = image.size

        print(fl)
        print(f"图像的宽度: {width} 像素")
        print(f"图像的高度: {height} 像素")
