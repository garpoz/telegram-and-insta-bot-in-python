#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

import time, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import create_image
from PIL import Image

create_image.main()

rnd = create_image.rnd
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
xc = im.width / 2
yc = im.height / 2
x1 = xc - 10
y1 = yc - 10
x2 = xc - 10
y2 = yc - 10
im = im.crop((x1, y1, x2, y2))
im=im.convert('RGB')
im.save("./story.jpg")
time.sleep(0.5)
shutil.copy("./story.png", f"./archive/{rnd}.png")

