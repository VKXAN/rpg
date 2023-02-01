import random
import time

import pyautogui as pag

while True:
    x = random.randint(700,900)
    y = random.randint(500,1000)

    pag.moveTo(x,y,0.000001)
    time.sleep(0.00001)
     