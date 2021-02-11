#! python

import pyautogui
import time

print("Press Ctrl-C to quit")
time.sleep(5)
try:
   while True:
       pyautogui.moveTo(100, 100, duration=0.25)
       pyautogui.moveTo(100, 200, duration=0.25)
       pyautogui.moveTo(200, 200, duration=0.25)
       pyautogui.moveTo(200, 100, duration=0.25)
       time.sleep(3)
except KeyboardInterrupt:
    print("\nDone")