import random
import os
import keyboard
import time
from interactClient import InteractClient
from ai import Ai
from decks import Decks










def main():
    global k
    k = 0
    print("Running")

    client.getFieldCords()




    while running:
        onLoop()

        if keyboard.is_pressed('esc'):
            os._exit(0)
        time.sleep(random.randint(15, 50) / 100)


def onLoop():
    global k
    global inGame

    while inGame:
        ai.onRun()











if __name__ == '__main__':
    running = True
    inGame = True
    butRegion = (0, 750, 800, 400)
    client = InteractClient(butRegion)
    deck = Decks([["Archer", 1], ["Poisoner", 5], ["Fire Mage", 1], ["Lightning Mage", 1], ["Cold Mage", 1]])
    ai = Ai(deck.cardData, client)
    main()
