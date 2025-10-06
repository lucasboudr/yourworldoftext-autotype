from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import random
import string
import pyautogui

amount = 0
chrome_driver_path = "/path/to/chromedriver"
current_datetime = datetime.now()


with open("words.txt", "r") as f:
    words = f.read().splitlines()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

for i, word in enumerate(words):
    driver.get(f"https://www.yourworldoftext.com/{word}")
    time.sleep(2)
    pyautogui.click(x=100, y=200)
    amount += 1
    pyautogui.write(f"This message was written the {current_datetime}, and in {amount} different pages", interval=0.02)

driver.quit()
