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
            return True
        else:
            return False

    def place(self):
        place = self.canPlace()

        if place[0] == 'can':
            self.click(place[1])
            return True
        else:
            return False

    def upgradeCard(self, cardImage):
        upgradeLocation = pyautogui.locateOnScreen(cardImage, confidence=0.9)

        if upgradeLocation != None:
            self.click(upgradeLocation)

    def getFieldCords(self):
        try:
            # find wall cords, then the stone markers, use that to find cords of each square
            topLeft = "./photos/topLeft.png"
            topRight = "./photos/topRight.png"
            bottomLeft = "./photos/bottomLeft.png"
            bottomRight = "./photos/bottomRight.png"
            centreStone1 = "./photos/centreStone1.png"
            centreStone = "./photos/centreStone.png"

            topLeft = pyautogui.locateAllOnScreen(topLeft, confidence=0.8)
            topRight = pyautogui.locateAllOnScreen(topRight, confidence=0.8)
            bottomLeft = pyautogui.locateAllOnScreen(bottomLeft, confidence=0.8)
            bottomRight = pyautogui.locateAllOnScreen(bottomRight, confidence=0.8)
            centreStone1 = pyautogui.locateAllOnScreen(centreStone1, confidence=0.8)
            centreStone = pyautogui.locateAllOnScreen(centreStone, confidence=0.8)


            for item in topLeft:
                if item.top >= 550:
                    topLeftItem = item
                    break

            for item in topRight:

                if item.top >= 550 and topLeftItem.left + 50 < item.left:
                    topRightItem = item
                    break

            for item in bottomLeft:
                if item.top >= topLeftItem.top + 50:
                    bottomLeftItem = item
                    break

            for item in bottomRight:
                # print(item)
                if item.top >= topLeftItem.top + 50 and bottomLeftItem.left + 50 < item.left:
                    bottomRightItem = item
                    break


            centreStones = []

            for item in centreStone:  # repeats same stone
                # print(item)
                if item.top >= topRightItem.top:
                    if len(centreStones) != 0:
                        if centreStones[-1].left + 5 < item.left or centreStones[-1].left - 5 > item.left:
                            centreStones.append(item)
                    else:
                        centreStones.append(item)

            centreStonesFinal = [centreStones[0]]
            for stone in centreStones:  # removes repeat stones
                passAmmount = 0
                stoneAmmount = len(centreStonesFinal)
                for item in centreStonesFinal:
                    itemLeft = item.left
                    itemTop = item.top
                    stoneLeft = stone.left
                    stoneTop = stone.top

                    # checks if stone in same range as item
                    if (stoneLeft > itemLeft - 5 and stoneLeft < itemLeft + 5) and (
                            stoneTop > itemTop - 5 and stoneTop < itemTop + 5):
                        break
                    else:
                        passAmmount += 1

                if passAmmount == stoneAmmount:
                    centreStonesFinal.append(stone)


            topStones = []
            bottomStones = []
            # put stones in order
            tallestStone = 0
            smallestStone = 2000

            field = [[], [], []]

            for i in range(len(centreStonesFinal)):
                if centreStonesFinal[i].top > tallestStone:
                    tallestStone = centreStonesFinal[i].top
                if centreStonesFinal[i].top < smallestStone:
                    smallestStone = centreStonesFinal[i].top

            for i in range(len(centreStonesFinal)):
                if centreStonesFinal[i].top > tallestStone - 5:
                    topStones.append(centreStonesFinal[i])
                if centreStonesFinal[i].top < smallestStone + 5:
                    bottomStones.append(centreStonesFinal[i])

            bottomStones = sorted(bottomStones, key=lambda box: box.left)
            topStones = sorted(topStones, key=lambda box: box.left)


            centreStonesFinal = []
            centreStonesFinal.append(bottomStones)
            centreStonesFinal.append(topStones)



            tileWidth = abs(centreStonesFinal[0][0].left - centreStonesFinal[0][1].left) - 15
            tileHeight = abs(centreStonesFinal[0][0].top - centreStonesFinal[1][0].top) - 20


            left = topLeftItem.left + 35
            top = topLeftItem.top + 35
            field[0].append([left, top, tileWidth, tileHeight])

            for i in range(4):
                left = centreStonesFinal[0][i].left + 15
                field[0].append([left, top, tileWidth, tileHeight])


            left = topLeftItem.left + 35
            top = centreStonesFinal[0][0].top + 15
            field[1].append([left, top, tileWidth, tileHeight])

            for i in range(4):
                left = centreStonesFinal[1][i].left + 15
                field[1].append([left, top, tileWidth, tileHeight])

            left = topLeftItem.left + 35
            top = centreStonesFinal[1][0].top + 15
            field[2].append([left, top, tileWidth, tileHeight])

            for i in range(4):
                left = centreStonesFinal[1][i].left + 15
                field[2].append([left, top, tileWidth, tileHeight])

        except Exception as e:
            print("Cant find field")
            print(e)
            pass

        return field

    def getUnitsOnField(self, field, cards):

        unitField = [[], [], []]
        for l in range(3):
            for k in range(5):
                data = None


                data = self.checkTileForCard(cards, field[l][k])

                unitField[l].append(data)

        return unitField

    def checkTileForCard(self, cards, tile):
        data = None
        for card in cards:
            cardPixel = card["locate color"]
            tileScreenshot = pyautogui.screenshot(region=tile)
            for x in range(tileScreenshot.width):
                for y in range(tileScreenshot.height):
                    gotPixel = tileScreenshot.getpixel((x, y))

                    if ((gotPixel[0] - 2 <= cardPixel[0]) and (gotPixel[0] + 2 >= cardPixel[0])) and (
                            (gotPixel[1] - 2 <= cardPixel[1]) and (gotPixel[1] + 2 >= cardPixel[1])) and (
                            (gotPixel[2] - 2 <= cardPixel[2]) and (gotPixel[2] + 2 >= cardPixel[2])):
                        data = card

                        break
                if data != None:
                    break

        return data

    def mergeUnits(self, moveFromTile, moveToTile):

        moveFromTile = self.randomiseClick(moveFromTile)
        moveToTile = self.randomiseClick(moveToTile)
        duration = random.randint(3, 8) / 10

        pyautogui.moveTo(moveFromTile[0], moveFromTile[1], duration=duration)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(moveToTile[0], moveToTile[1], duration=duration)
        pyautogui.mouseUp(button='left')

    def upgradeUnit(self, unit):
        upgrade = pyautogui.locateOnScreen(unit["can upgrade pic"], confidence=0.9)

        if upgrade != None:
            self.click(upgrade)

            pyautogui.moveTo(100, 100, duration=0.2)
            return True
        else:
            return False

    def click(self, details):
        if True:
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

