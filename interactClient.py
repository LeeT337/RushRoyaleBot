import pyautogui
import random

class InteractClient:

    def __init__(self, butRegion):
        self.butRegion = butRegion

    def canPlace(self):

        canPlace = pyautogui.locateOnScreen("photos/canPlace.png", confidence=0.9, region=self.butRegion)
        cantPlace = pyautogui.locateOnScreen("photos/cantPlace.png", confidence=0.9, region=self.butRegion)
        if canPlace != None:

            cords = canPlace
            # print(cords)
            return ["can", cords]
            # return "Can place"


        elif cantPlace != None:
            cords = self.cantPlace
            # print(cords)
            # return cantPlace
            return ["Cant"]


        else:
            return ["Not in game"]

    def startPlay(self):
        play = pyautogui.locateOnScreen("photos/play.png", confidence=0.9)
        if play != None:
            c = self.randomiseClick(play)
            pyautogui.click(c[0], c[1])

    def place(self):
        place = self.canPlace()

        if place[0] == 'can':
            self.click(place[1])


    def click(self, details):
        ran = self.randomiseClick(details)
        x = ran[0]
        y = ran[1]
        pyautogui.click(x=x, y=y)

    def randomiseClick(self, details):  # details = (left, top, width, height)
        left = details[0]
        top = details[1]
        width = details[2]
        height = details[3]
        x = random.randint(left, left + width)
        y = random.randint(top, top + height)
        return (x, y)