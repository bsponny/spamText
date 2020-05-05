# Pyautogui: https://pyautogui.readthedocs.io/en/latest/install.html

import pyautogui
import time

# this is used to give you time to open up the messages app and click into the text box.
time.sleep(3)

# Specify what text file to use.
file = open("docs/test.txt")

for words in file:
    word = words.split()
    for i in word:
        pyautogui.write(i)
        pyautogui.press('enter')
        time.sleep(0.001)