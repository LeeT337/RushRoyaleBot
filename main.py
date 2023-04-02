import pyautogui
import pynput
import random
import os
import keyboard
import time
import pydirectinput
from pynput.mouse import Button, Controller as MouseController
from interactClient import InteractClient










def main():
    global k
    k = 0
    print("Running")

    #print(client.canPlace())


    while running:
        onLoop()

        if keyboard.is_pressed('esc'):
            os._exit(0)
        time.sleep(random.randint(15, 50) / 100)


def onLoop():
    global k
    #screenshot = pyautogui.screenshot(region=butRegion)
    #screenshot = pyautogui.screenshot()
    client.startPlay()
    client.place()






if __name__ == '__main__':
    running = True
    butRegion = (0, 750, 800, 400)  # Create algorithm where user enters window dimensions, e.g. positon, length, height and it calcs which part of screen button on
    client = InteractClient(butRegion)
    main()
