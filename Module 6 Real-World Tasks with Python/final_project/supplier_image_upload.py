#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = "./supplier-data/images/" 
for image in os.listdir(path):
    if image.endswith(".jpeg"):
        with open(path + image, "rb") as opened_jpg:
            try:
                response = requests.post(url, files = {"file": opened_jpg})
                print(response.url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
            print("Image uploaded successfully : ", image)
            opened_jpg.close()
            