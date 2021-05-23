import webbrowser

import pyautogui
import webbrowser
import time

print("you have to wait for 25 seconds for it to start ")

fword = input("enter the first word or sentences to be spammed")






webbrowser.open_new("https://web.whatsapp.com/")
time.sleep(30
)

# ENTER THE AMOUNT OF TIMES YOU WANT TO SPAM AFTER range ie range(x)
for i in range(1000000):
    pyautogui.typewrite(fword)
    pyautogui.press("enter")

