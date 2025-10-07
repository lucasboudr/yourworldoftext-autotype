from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
import pyautogui

# Configuration 
chrome_driver_path = r"C:\Users\lucas\Documents\GitHub\yourworldoftext\chromedriver.exe"
use_list = True  # If True, go through all pages in words.txt
page_name = "67"  # Page to write on (e.g. https://www.yourworldoftext.com/67)
delay = 0.02      # Delay between each keystroke
amount = 0        # Starting counter

# Load word list if enabled
with open("words.txt", "r") as f:
    words = f.read().splitlines()

# Set up Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Current date 
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main Logic
if use_list:
    for word in words:
        driver.get(f"https://www.yourworldoftext.com/{word}")
        time.sleep(2)
        pyautogui.click(x=100, y=200)
        amount += 1
        text = f"Hello world!\nThis message was written {amount} times\nThis message was written on {current_date}"
        pyautogui.write(text, interval=delay)
else:
    driver.get(f"https://www.yourworldoftext.com/{page_name}")
    time.sleep(2)
    pyautogui.click(x=100, y=200)
    amount += 1
    text = f"Hello world!\nThis message was written {amount} times\nThis message was written on {current_date}"
    pyautogui.write(text, interval=delay)

driver.quit()
