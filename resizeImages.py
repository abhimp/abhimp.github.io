import os
import glob
import cv2
import numpy as np
import hashlib
from exif import Image as eximg
import json

imageMd5Sum = {}
# imageStat = {}

def findListofImagestobeReduced():
    curdir = os.getcwd()
    os.chdir("./travelImages/")
    images = glob.glob("*/*/orig/*")
    os.chdir(curdir)
    names = [(os.path.dirname(os.path.dirname(x)), os.path.basename(x), x) for x in images]
    names = [(os.path.join("travelImages", x[0], "reduced", x[1]), os.path.join("travelImages", x[2]), os.path.join("travelImages", x[0], "moded", x[1])) for x in names]
    return names

def matchMD5Sum(imgPath, sumPath):
    hash = ""
    m = hashlib.md5()
    m.update(open(imgPath, "rb").read())
    hash = m.hexdigest()
    oldHash = ""
    if os.path.isfile(sumPath):
        oldHash = open(sumPath).read().strip()
    if oldHash != hash:
        sumDir = os.path.dirname(sumPath)
        if not os.path.isdir(sumDir):
            os.makedirs(sumDir)
        with open(sumPath, "w") as fp:
            fp.write(hash)
        # print(imgPath, False)
        return False
    # print(imgPath, True, [oldHash, hash])
    return True

def getMD5Sum(imgPath):
    if imgPath in imageMd5Sum:
        return imageMd5Sum[imgPath]

    m = hashlib.md5()
    m.update(open(imgPath, "rb").read())
    hash = m.hexdigest()
    imageMd5Sum[imgPath] = hash
    return hash

def verifyUsingExifData(origPath, waterPath):
    if not os.path.isfile(waterPath):
        return False

    im = eximg(waterPath)
    if not im.has_exif:
        return False

    dt = im.get("make")

    if dt is None:
        return False
    dt = json.loads(dt)
    oldHash = dt.get("am_hash")
    oldMtime = dt.get("am_mtime")
    oldSize = dt.get("am_size")

    if oldHash is None or oldMtime is None or oldSize is None:
        return False

    st = os.stat(origPath)
    if oldSize != st.st_size:
        return False

    if oldHash != getMD5Sum(origPath):
        return False

    return True

def saveWithExif(origPath, origWaterPath, img, comp):
    status, image_jpg_coded = cv2.imencode('.jpg', img, comp)
    assert(status)
    image_jpg_coded_bytes = image_jpg_coded.tobytes()
    exif_jpg = eximg(image_jpg_coded_bytes)
    # exif_jpg.has_exif = True
    dt = {}
    dt["am_hash"] = getMD5Sum(origPath)
    dt["am_mtime"] = os.stat(origPath).st_mtime
    dt["am_size"] = os.stat(origPath).st_size
    exif_jpg["make"] = json.dumps(dt)

    # print(exif_jpg.list_all())

    new_image_file = open(origWaterPath, "wb")
    new_image_file.write(exif_jpg.get_file())

def reduceImage(reducedPath, origPath, origWaterPath):
    if verifyUsingExifData(origPath, origWaterPath):
        return
    print(f"Reducing {origWaterPath} to {reducedPath}")
    origDir = os.path.dirname(origWaterPath)
    reduceDir = os.path.dirname(reducedPath)
    if not os.path.isdir(origDir):
        os.makedirs(origDir)
    if not os.path.isdir(reduceDir):
        os.makedirs(reduceDir)
    MAX_HEIGHT = 1200
    im = cv2.imread(origPath)
    h,w,_ = im.shape
    nh = MAX_HEIGHT
    nw = int(w*MAX_HEIGHT/h + 0.5)
    # img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    blank = np.zeros(shape=(nh, nw, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank,
            text='abhijitmondal.in',
            org=(blank.shape[1] - 240, blank.shape[0] - 60),
            fontFace=font,
            fontScale= .8,color=(255,255,255),
            thickness=1,
            lineType=cv2.LINE_4)
    nim = im
    if h < MAX_HEIGHT:
        nw = int(nw*h/MAX_HEIGHT + 0.5)
        nh = h
        blank = cv2.resize(blank, [nw, nh])
        # nim = im
    else:
        nim = cv2.resize(im, [nw, nh])
    mask = cv2.bitwise_not(blank)
    blend = cv2.bitwise_and(nim, mask)
    blend = cv2.bitwise_or(blend, blank)
    comp = [cv2.IMWRITE_JPEG_QUALITY, 86, cv2.IMWRITE_PNG_COMPRESSION, 7]
    # cv2.imwrite(origWaterPath, blend, comp)
    saveWithExif(origPath, origWaterPath, blend, comp)
    h,w,_ = im.shape
    nw = int(w*200/h + 0.5)
    nim = cv2.resize(im, [nw,200])
    cv2.imwrite(reducedPath, nim, comp)




for x in findListofImagestobeReduced():
    # print(x)
    # print(f"Reducing {x[1]} to {x[0]}")
    reduceImage(*x)
    # exit(0)

