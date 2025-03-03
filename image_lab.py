#!/usr/bin/env python3
import os
from PIL import Image
old_path = os.path.expanduser('~/images/')
new_path = '/opt/icons/'


def main():
    for image in os.listdir(old_path):
        print("Processing image: ", image)
        if image == '.DS_Store':
            continue
        with Image.open(old_path + image) as img:
            img = img.rotate(-90).resize((128, 128)).convert('RGB')
            img.save(new_path + image, 'jpeg')
            img.close()
            print("Image saved as: ", new_path + image)


if __name__ == '__main__':
    main()