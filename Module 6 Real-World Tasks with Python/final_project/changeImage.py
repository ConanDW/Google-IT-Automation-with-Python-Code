#!/usr/bin/env python3
from PIL import Image
import os

path = "./supplier-data/images/"

for image in os.listdir(path):
    if image.endswith(".tiff"):
        with Image.open(path + image) as img:
            new_image = img.convert("RGB")
            new_image = new_image.resize((600, 400))
            new_image.save(path + image.split(".")[0] + ".jpeg", "JPEG")
            new_image.close()