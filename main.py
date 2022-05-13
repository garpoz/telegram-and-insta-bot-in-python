#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

import time, shutil, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import create_image
from PIL import Image


os.system("cls" if os.name == "nt" else "clear")
create_image.main()

rnd = create_image.rnd
noe = create_image.noe
chrome_options = Options()
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
chrome_options.headless = True

chrome_options.add_argument(f"user-agent={agent}")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
d = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
d.get(
    "file:///home/behrouz/ptn_pro/kar_lanser/telegram-and-insta-bot-in-python/format/index.html"
)

S = lambda X: d.execute_script("return document.body.parentNode.scroll" + X)
d.set_window_size(S("Width"), S("Height"))
time.sleep(0.5)
d.get_screenshot_as_file("./story.png")
d.quit()
time.sleep(0.5)
im = Image.open("./story.png")
xc, yc = im.size
ppix = im.load()
for i in range(xc):
    if str(ppix[i, 50]) == "(0, 0, 0, 255)":
        break
i -= 2
if i < 0:
    i = 0
for z in range(yc):
    if str(ppix[200, z]) == "(0, 0, 0, 255)":
        break
z -= 2
if z < 0:
    z = 0
im = im.crop((i, 5, xc - i, yc - 5))
im.save("./story.png")
time.sleep(0.5)
if noe == "roze":
    noe = "1"
else:
    noe = "2"
shutil.copy("./story.png", f"./archive/{noe}/{rnd}.png")
