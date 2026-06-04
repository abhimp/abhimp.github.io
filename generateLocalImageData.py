import os
import json
import hashlib
import glob
from exif import Image as eximg
from PIL import Image


def getLatlong(imgPath):
    im = eximg(imgPath)
    infoJson = im.get_all()
    data = {}
    if "gps_latitude" not in infoJson or "gps_latitude_ref" not in infoJson:
        return None

    lat = infoJson["gps_latitude"]
    lat = "%d°%d'%g\""%lat
    lat += infoJson["gps_latitude_ref"]

    if "gps_longitude" not in infoJson or "gps_longitude_ref" not in infoJson:
        return None

    lng = infoJson["gps_longitude"]
    lng = "%d°%d'%g\""%lng
    lng += infoJson["gps_longitude_ref"]

    data = {"lat": lat, "lng": lng, "url": f"https://maps.google.com/?q={lat}+{lng}"}

    alt = infoJson.get("gps_altitude", None)
    time = infoJson.get("gps_timestamp", None)
    date = infoJson.get("gps_datestamp", None)

    for x, y in [("alt", alt), ("time", time), ("date", date)]:
        if y is not None:
            data[x] = y

    return data

def getImagePaths(imgYearPath, year):
    curpath = os.getcwd()
    os.chdir(imgYearPath)
    images = glob.glob(f"*/*") + glob.glob(f"*/*/*")
    keys = [f"images/travel/" + img.split(os.path.sep, 1)[0] + "/./" + img.split(os.path.sep, 1)[1] for img in images]
    images = [f"{imgYearPath}/{x}" for x in images]
    os.chdir(curpath)
    return zip(keys, images)



def main():
    imageBase = "travelImages"

    years = os.listdir("_wpages/travel/")

    imgData = {}

    fileName = "_data/images.json"

    for y in years:
        imgYearPath = os.path.join(imageBase, y)
        print(imgYearPath)
        if not os.path.exists(imgYearPath) or not os.path.isdir(imgYearPath):
            continue
        images = getImagePaths(imgYearPath, y)
        for key, img in images:
            if os.path.isdir(img):
                continue
            try:
                im = Image.open(img)
                if im is None:
                    continue
                w, h = im.size
            except:
                print("img: ", img)
                continue
            gps = getLatlong(img)

            hash = ""
            mtime = "" #os.stat(x).st_mtime
            imgData["/"+key] = {"dim": [w,h], "mtime": mtime, "hash": hash}
            if gps is not None:
                imgData["/"+key]["gps"] = gps

    imgFullData = {
        "metadata": {
            "base": "/"+imageBase+"/",
            "thumb": ".",
            "full": "."
        },
        "data": imgData
    }

    with open(fileName, "w") as fp:
        json.dump(imgFullData, fp)

    print("Dumped into", fileName)

main()