# Pyautogui: https://pyautogui.readthedocs.io/en/latest/install.html

import pyautogui
import time
import os

dirs = os.listdir("docs/")

print("What file do you want to use? (ex. test.txt)")
print("\tFiles Available for Use:")
for file in dirs:
    print("\t\t" + file)

fileName = input()

speed = 2
print("Click on the message box")

# this is used to give you time to open up the messages app and click into the text box.
time.sleep(6)

file = open("docs/" + fileName)

for words in file:
    word = words.split()
    for i in word:
        pyautogui.write(i)
        pyautogui.press('enter')
        time.sleep(speed)
print("Thanks for Playing!")