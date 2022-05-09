#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
mobile_emulation = {"deviceName": "Galaxy S5"}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument(f"user-agent={agent}")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
d = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
d.get("https://www.instagram.com/")
time.sleep(5)
d.find_element_by_xpath("//input[@name='username']").send_keys("behrooz_ashraf")
d.find_element_by_xpath("//input[@name='password']").send_keys("*********")
d.find_element_by_xpath("//div[contains(text(),'Log In')]").click()
time.sleep(10)
d.find_element_by_xpath("//button[normalize-space()='Save Info']").click()
time.sleep(10)
d.find_element_by_xpath("//img[@class='_6q-tv']").send_keys('./image.png')
time.sleep(5)
d.get_screenshot_as_file("./story.png")
d.quit()
