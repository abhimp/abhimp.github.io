import urllib.request
import json
import os

years = [2021, 2022, 2023]
years = os.listdir("_wpages/travel/")

imgData = {}

fileName = "_data/images.json"

print(os.getcwd())

for y in years:
    try:
        fp = urllib.request.urlopen(f"https://abhimp.gitlab.io/trimg{y}/images.json")
        js = json.load(fp)
        print("Loading", y, len(imgData), "+", len(js), end=" ")
        imgData.update(js)
        print("=", len(imgData))
    except urllib.error.HTTPError:
        print(f"Could not fetch {y}")

with open(fileName, "w") as fp:
    json.dump(imgData, fp)

print("Dumped into", fileName)
