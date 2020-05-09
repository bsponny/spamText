import pyautogui
import time

name = input("Enter the name of the person: ")
gen = input("What pronoun should we use? Type 'he' or 'she': ")
speed = 2

# this is used to give you time to open up the messages app and click into the text box.
time.sleep(6)

pyautogui.write("Welcome to \"Let's See How High We Can Count Before " + name + " Responds!\" I'm your host Brock Sponenburgh!")
pyautogui.press('enter')
time.sleep(speed)

pyautogui.write("You know the rules, if " + name + " responds before we count to 100, " + gen + " wins, if not, we win!")
pyautogui.press('enter')
time.sleep(speed)

pyautogui.write("Now. LET'S GET COUNTING!!")
pyautogui.press('enter')
time.sleep(speed)

for i in range (1, 101):
    pyautogui.write(str(i))
    pyautogui.press('enter')
    time.sleep(speed)
