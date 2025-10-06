> [!IMPORTANT]
> This is a small project I made for my own learning experience with Python.  
> It’s my **first Python project**, made just for practice — so it won’t have long-term support or updates.

### 🧠 YourWorldOfText Autotype

A small automation tool that types text automatically in [YourWorldOfText](https://www.yourworldoftext.com/).  
It uses **Selenium** and **PyAutoGUI** to simulate typing and mouse clicks, made purely for **learning and experimentation**.

* My **first Python project**
* Built for **learning automation**
* Uses **Selenium** and **PyAutoGUI**
* **No long-term maintenance** — just for fun and experience

[![python-version-shield](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white&labelColor=black)](https://www.python.org/)
[![license-shield](https://img.shields.io/badge/license-MIT-green?labelColor=black)](LICENSE)

---

## ⚙️ Setup Instructions

### 🧩 Requirements

Before running the script, make sure you have the following installed:

- **Python 3.x**
- **Google Chrome browser**
- **Python packages:**
  - selenium  
  - pyautogui

If you don’t have them installed, simply run:

    pip install selenium pyautogui

---

### 🛠️ Setup

1. **Download ChromeDriver** that matches your current version of Google Chrome:  
   🔗 https://chromedriver.chromium.org/downloads  
2. Copy the **full path** to your downloaded ChromeDriver.  
3. Open the script and replace this line:

       chrome_driver_path = "/path/to/chromedriver"

   with your actual path. Example:

       chrome_driver_path = r"C:\Users\Lucas\Downloads\chromedriver.exe"

4. The provided `words.txt` file contains the list of words or phrases that will be typed automatically.  
   You can edit this file to customize what the script types (one line per entry).

---

### ▶️ Running the Script

You can run the script by either:

- **Double-clicking** the `.py` file, or  
- Running it manually from the terminal:

      python script.py

When you run it, the script will open **YourWorldOfText** in Chrome and begin typing each entry from `words.txt` automatically.

---

### 📝 Notes

If the script clicks in the wrong place, adjust this line in your code:

      pyautogui.click(x=100, y=200)

You can change the coordinates until the cursor clicks inside the typing area on the site.

---

### 💭 Final Thoughts

This is my **first Python project**, made to learn browser automation and scripting basics.  
It’s a fun little experiment with Python, Selenium, and PyAutoGUI — feel free to explore and improve it!
