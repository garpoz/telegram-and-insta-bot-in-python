#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

import time, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import create_image

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
time.sleep(1)
d.get_screenshot_as_file("./story.png")
d.quit()

shutil.copy("./story.png", f"./archive/{rnd}.png")
