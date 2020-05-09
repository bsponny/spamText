# Pyautogui: https://pyautogui.readthedocs.io/en/latest/install.html

import pyautogui
import time

fileName = input("What file do you want to use? (ex. test.txt) ")

# this is used to give you time to open up the messages app and click into the text box.
time.sleep(6)

file = open("docs/" + fileName)

for words in file:
    word = words.split()
    for i in word:
        pyautogui.write(i)
        pyautogui.press('enter')
        time.sleep(2)
