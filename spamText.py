## Dependancies: pyautogui, Python3
## Pyautogui: https://pyautogui.readthedocs.io/en/latest/install.html
## Python3: https://www.python.org/downloads/
import pyautogui
import time

## Replace this with what you would like to spam one word at a time.
words = "This is the test string"

## this is used to give you time to open up the messages app and click into the text box.
time.sleep(3)

## Split the "Lyrics" string into individual words
word = words.split()
x = range(len(word))
for i in word:
    pyautogui.write(i)
    pyautogui.press('enter')
    time.sleep(0.001)