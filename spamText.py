## Dependancies: pyautogui, Python3
## Pyautogui: https://pyautogui.readthedocs.io/en/latest/install.html
## Python3: https://www.python.org/downloads/
import pyautogui
import time

## Replace this with what you would like to spam one word at a time.
lyrics = "Fill em with the venom and eliminate em Other words, I Minute Maid em I dont wanna hurt em, but I did em in a fit of rage Im murderin again, nobody will evade him Finna kill em and dump all the fuckin bodies in the lake Obliterating everything, incinerate and renegade em And I make anybody who want it with the pen afraid But dont nobody want it, but theyre gonna get it anyway Cause Im beginnin to feel like Im mentally ill Im Atilla, kill or be killed, Im a killer bee, the vanilla gorilla Youre bringin the killer within me out of me You dont want to be the enemy of the demon who went in me Or being the recievin end of me, what stupidity itd be Every bit of me is the epitome of a spitter When Im in the vicinity, motherfucker, you better duck Or you finna be dead the minute you run into me A hunnid percent of you is a fifth of a percent of me Im bout to fuckin finish you bitch, Im unfadable You wanna battle, Im available, Im blowin up like an inflatable Im undebatable, Im unavoidable, Im unevadable Im on the toilet bowl, I got a trailer full of money and Im paid in full Im not afraid to pull the Man, stop Look what Im plannin, haha "

## this is used to give you time to open up the messages app and click into the text box.
time.sleep(3)
## Split the "Lyrics" string into individual words
lyric = lyrics.split()
x = range(len(lyric))
for i in lyric:
    pyautogui.write(i)
    pyautogui.press('enter')
    time.sleep(0.001)