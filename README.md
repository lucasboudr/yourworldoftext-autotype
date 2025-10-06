Setup Instructions

Requirements
Before running the script, make sure you have the following installed:

- Python 3.x
- Google Chrome browser
- The following Python packages:
selenium and pyautogui
if you dont have them installed just run
pip install selenium pyautogui

Setup

1. Download ChromeDriver that matches your current version of Google Chrome:
https://chromedriver.chromium.org/downloads
2. Copy the full path to your downloaded ChromeDriver.
3. Open the script and replace this line:
chrome_driver_path = "/path/to/chromedriver"
with the actual path to your ChromeDriver. Example:
chrome_driver_path = r"C:\Users\YourName\Downloads\chromedriver.exe"
4. The provided words.txt file already contains the list of page names the script will use.
You can edit this file to customize which pages it posts to (one word per line).

Run the script double left click on the file or run python script.py

Notes

If the script clicks in the wrong place, adjust the line:
pyautogui.click(x=100, y=200)
