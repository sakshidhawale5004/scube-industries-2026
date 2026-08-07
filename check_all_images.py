import urllib.request
import urllib.parse

images = [
    "ALLIGATOR GRAB.png",
    "BLIND BOX.png",
    "BULL DOG SPEAR.png",
    "FLUTED CENTRALISER.png",
    "HYDROSTATIC BAILER.png",
    "IMPRESSION BLOCK.png",
    "JD PULLING TOOL.png",
    "MAGNETIC FISHING TOOL.png",
    "PULLING TOO R SERIES.png",
    "PULLING TOOL S SERIES.png",
    "RELEASABLE OVERSHOT.PNG",
    "SAND PUMP BAILER.png",
    "SELF RELEASING OVERSHOT.png",
    "SIDE WALL CUTTER.png",
    "SKATE SYSTEM.png",
    "WIRELINE FISHING MAGNET.png",
    "WIRELINE OVERSHOT.png",
    "WIRELINE SPEAR.png"
]

base_url = "https://scube-industries-2026.vercel.app/foldertoadd/"

all_good = True
for img in images:
    url = base_url + urllib.parse.quote(img)
    try:
        req = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(req)
        if response.getcode() != 200:
            print(f"FAILED: {img} - Status: {response.getcode()}")
            all_good = False
    except Exception as e:
        print(f"ERROR: {img} - {e}")
        all_good = False

if all_good:
    print("ALL 18 IMAGES ARE LIVE AND RETURN 200 OK!")
