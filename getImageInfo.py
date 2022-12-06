import os
import cv2
import json
import hashlib
import glob


def findListofImages():
    curdir = os.getcwd()
    os.chdir("./travelImages/")
    images = glob.glob("*/*/orig/*")
    os.chdir(curdir)
    names = [(os.path.dirname(os.path.dirname(x)), os.path.basename(x), x) for x in images]
    names = [(os.path.join("images/travel", x[0], "reduced", x[1]), os.path.join("travelImages", x[0], "moded", x[1])) for x in names]
    return names


def loadOldData():
    try:
        fp = open("_data/images.json", "r")
        data = json.load(fp)
        fp.close()
        return data
    except:
        return {}

oldDt = loadOldData()

dt = {}
readinNew = 0
skiping = 0
for key, x in findListofImages():
    hash = ""
    m = hashlib.md5()
    m.update(open(x, "rb").read())
    hash = m.hexdigest()
    mtime = "" #os.stat(x).st_mtime
    oldX = "/" + key
    if oldX in oldDt:
        if hash == oldDt[oldX]["hash"]:
            dt[oldX] = oldDt[oldX]
            skiping += 1
            continue
    im = cv2.imread(x)
    if im is None:
        print(x)
        continue
    readinNew += 1
    h,w,_ = im.shape
    dt["/"+key] = {"dim": [w,h], "mtime": mtime, "hash": hash}

if readinNew > 0:
    fp = open("_data/images.json", "w")
    json.dump(dt, fp)
    fp.close()

print(readinNew, skiping)