import urllib.request
import json
import os

years = [2021, 2022]

imgData = {}

fileName = "_data/images.json"

print(os.getcwd())

for y in years:
    fp = urllib.request.urlopen(f"https://abhimp.gitlab.io/trimg{y}/images.json")
    js = json.load(fp)
    print("Loading", y, len(imgData), "+", len(js), end=" ")
    imgData.update(js)
    print("=", len(imgData))

with open(fileName, "w") as fp:
    json.dump(imgData, fp)

print("Dumped into", fileName)
