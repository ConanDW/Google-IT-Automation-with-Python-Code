#! /usr/bin/env python3
import os
import requests

text_path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"
keys = ["name", "weight", "description", "image_name"]

for text_file in os.listdir(text_path):
    print(f"Processing file: {text_file}")
    fruits = {}
    with open(os.path.join(text_path, text_file)) as f:
        lines = f.readlines()
        if len(lines) != 3:
            print(f"Skipping file due to unexpected format: {text_file}")
            continue
        
        fruits["name"] = lines[0].strip()
        try:
            fruits["weight"] = int(lines[1].strip().replace("lbs", "").strip())
        except ValueError:
            print(f"Skipping file due to invalid weight value: {text_file}")
            continue
        fruits["description"] = lines[2].strip()
        
        # Find the corresponding image file
        image_name = os.path.splitext(text_file)[0] + ".jpeg"
        if image_name in os.listdir(img_path):
            fruits["image_name"] = image_name
        else:
            print(f"No image found for {fruits['name']}, skipping upload.")
            continue
        
        # Upload the JSON data
        try:
            response = requests.post("http://35.229.125.53/fruits/", json=fruits)
            response.raise_for_status()
            if response.status_code == 201:
                print(f"Successfully uploaded: {fruits}")
            else:
                print(f"Failed to upload: {fruits}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")