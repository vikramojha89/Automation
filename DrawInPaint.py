#! python
#
# Copyright (C) https://automatetheboringstuff.com/
#
#2/12/2021: Initial Commit

import pyautogui
import time

print("Press Ctrl-C to quit")
time.sleep(5)
try:
   pyautogui.click()   #click to put drawing to focus
   distance = 200
   while distance > 0:
       pyautogui.dragRel(distance, 0, duration=0.25) #move right
       distance = distance - 5
       pyautogui.dragRel(0, distance, duration=0.25) #move down
       pyautogui.dragRel(-distance, 0, duration=0.25) #move left
       distance = distance - 5
       pyautogui.dragRel(0, -distance, duration=0.25) #move up
       
except KeyboardInterrupt:
    print("\nDone")