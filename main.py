import sys
import requests
from PIL import Image, ImageDraw, ImageFont

fontsize = 18
fnt = ImageFont.truetype("Makinas-4-Square.otf",fontsize)
ch = 400211

def getId():
    data = requests.get("http://192.168.0.98:8888/api/programss").json()

    print(type(len(data)))
    for i in range(len(data)):
        print(str(data[i]["id"]) + str(data[i]["name"]))



def getProgramName():
    data = requests.get("http://192.168.0.98:8888/api/schedule/broadcasting?time=0").json()
    for i in range(len(data)):
        if(ch == data[i]["programs"][0]["channelId"]):
            pname = str(data[i]["programs"][0]["name"])
            return pname;

print(getProgramName())

with Image.open("testpic.jpeg") as im: #imageを開く。closeを自動でやってくれるよ
    print(im.format, im.width, im.height, im.mode)
    d = ImageDraw.Draw(im)
    d.text((1300,im.height - fontsize *1.5), "ねこ", font=fnt, fill=(0,0,0,128))
    im.save("pic.jpeg", "PNG")