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
<<<<<<< HEAD
speed = 2
print("Click on the message box")
=======
speed = 3
>>>>>>> 83b1d523a8beac63156c83f9b83bc1e21d57a407

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