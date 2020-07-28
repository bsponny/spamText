import pyautogui, time, msvcrt

name = input("Enter the name of the person: ")
gen = input("What pronoun should we use? Type 'he' or 'she': ")
number = int(input("How high would you like to count? "))
message = "Click on the message box"
speed = 3

# this is used to give you time to open up the messages app and click into the text box.
print(message)
time.sleep(6)

pyautogui.write("Welcome to \"Let's See How High We Can Count Before " + name + " Responds!\" I'm your host Brock Sponenburgh!")
pyautogui.press('enter')
time.sleep(speed)

pyautogui.write("You know the rules, if " + name + " responds before we count to " + str(number) + ", " + gen + " wins, if not, we win!")
pyautogui.press('enter')
time.sleep(speed)

pyautogui.write("Now. LET'S GET COUNTING!!")
pyautogui.press('enter')
time.sleep(speed)

for i in range (1, number + 1):
    pyautogui.write(str(i))
    pyautogui.press('enter')
    time.sleep(speed / 2)

response = True
while (response == True):
    end = input("Did " + name + " win (1) or lose (2)? ")
    if end == "1":
        print(message)
        time.sleep(6)
        pyautogui.write("Sorry " + name + ", it looks like you lost.")
        pyautogui.press('enter')
        time.sleep(speed)
        response = False
    elif end == "2":
        print(message)
        endNum = input("What number did you stop at? ")
        time.sleep(6)
        pyautogui.write("Congrats " + name + " YOU WON!!! We counted to " + endNum + ".")
        pyautogui.press('enter')
        time.sleep(speed)
        response = False
    else:
        print("Sorry. That is not a valid response. Try again.")
        response = True

pyautogui.write("I'm your host Brock Sponenburgh! Thanks for playing! And we'll see you next time on \"Let's See How High We Can Count Before " + name + " Responds!\"")
pyautogui.press('enter')