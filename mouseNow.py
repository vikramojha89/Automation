#! python

import pyautogui
import time

print("Press Ctrl-C to quit")
time.sleep(5)
try:
   while True:
       #TODO: Get and print the mouse co-ordinates
       #x, y = pyautogui.position()
       #positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
       #print(positionStr, end="")
       #print('\b'*len(positionStr), end="", flush=True)
       pyautogui.click(103, 360, button="left") #for login
       pyautogui.click(991, 113, button="left") #click on send button`
       time.sleep(1)
       pyautogui.click(111, 470, button="left") #for logout
       pyautogui.click(991, 113, button="left") #click on send button
       time.sleep(1)
except KeyboardInterrupt:
    print("\nDone")