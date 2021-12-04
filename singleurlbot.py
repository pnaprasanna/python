import time, urllib
#url = "https://docs.python.org/3/ddd"
#url2 = "https://pna.konagam"
url1 = "https://www.google.com"
while True:
    try:
        urllib.urlopen(url1)
        print("success")
    except:
        print("error")
    time.sleep(3)
