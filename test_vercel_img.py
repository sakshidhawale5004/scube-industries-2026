import urllib.request

url = "https://scube-industries-2026.vercel.app/foldertoadd/ALLIGATOR%20GRAB.png"
try:
    response = urllib.request.urlopen(url)
    print(f"Status Code: {response.getcode()}")
except Exception as e:
    print(f"Error: {e}")
