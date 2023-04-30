import json

class Ai:
    def __init__(self, deck, client):
        self.client = client
        self.deck = deck
        self.attackUnit1 = deck[0]
        self.attackUnit2 = deck[1]
        self.supportAttackUnit1 = deck[2]
        self.supportAttackUnit2 = deck[3]
        self.supportUnit1 = deck[4]
        self.attackUnit1Data = {"ammount units": 0, "unit lvl": 1, "locations": []}
        self.attackUnit2Data = {"ammount units": 0, "unit lvl": 1, "locations": []}
        self.supportAttackUnit1Data = {"ammount units": 0, "unit lvl": 1, "locations": []}
        self.supportAttackUnit2Data = {"ammount units": 0, "unit lvl": 1, "locations": []}
        self.supportUnit1Data = {"ammount units": 0, "unit lvl": 1, "locations": []}
        self.mana = 0
        self.moralePercent = 100
        self.canUseHero = True
        self.placeCost = 50
        self.upgradeCosts = [100, 200, 400, 700]
        self.attackUnitsOnField = 0
        self.defenceUnitsOnField = 0
        self.totalUnits = 0
        self.loops = 0


        self.fieldLocation = self.client.getFieldCords()

        self.fieldWithCards = client.getUnitsOnField(self.fieldLocation, self.deck)

        r = 0

        self.updateUnitData()



    def onRun(self):

        self.onLoop()

    def onLoop(self):
        self.loops += 1


        self.minUnits()
        if (self.loops % 5 == 0):
            self.fieldWithCards = self.client.getUnitsOnField(self.fieldLocation, self.deck)

            self.updateUnitData()

        if (self.loops % 10 == 0):

            self.merge()







    def updateUnitData(self):
        self.attackUnit1Data["ammount units"] = 0
        self.attackUnit2Data["ammount units"] = 0
        self.supportAttackUnit1Data["ammount units"] = 0
        self.supportAttackUnit2Data["ammount units"] = 0
        self.supportUnit1Data["ammount units"] = 0
        self.attackUnit1Data["locations"] = []
        self.attackUnit2Data["locations"] = []
        self.supportAttackUnit1Data["locations"] = []
        self.supportAttackUnit2Data["locations"] = []
        self.supportUnit1Data["locations"] = []
        for i in range(len(self.fieldWithCards)):
            for k in range(len(self.fieldWithCards[i])):
                if self.fieldWithCards[i][k] != None:
                    if self.fieldWithCards[i][k]["name"] == "Archer":
                        self.attackUnit1Data["ammount units"] += 1
                        self.attackUnit1Data["locations"].append([i, k])

                    elif self.fieldWithCards[i][k]["name"] == "Poisoner":
                        self.attackUnit2Data["ammount units"] += 1
                        self.attackUnit2Data["locations"].append([i, k])

                    elif self.fieldWithCards[i][k]["name"] == "Fire Mage":
                        self.supportAttackUnit1Data["ammount units"] += 1
                        self.supportAttackUnit1Data["locations"].append([i, k])

                    elif self.fieldWithCards[i][k]["name"] == "Lightning Mage":
                        self.supportAttackUnit2Data["ammount units"] += 1
                        self.supportAttackUnit2Data["locations"].append([i, k])

                    elif self.fieldWithCards[i][k]["name"] == "Cold Mage":
                        self.supportUnit1Data["ammount units"] += 1
                        self.supportUnit1Data["locations"].append([i, k])

                    self.totalUnits += 1




    def minUnits(self):
        next = True



        if self.attackUnit1Data["ammount units"] < 2 or self.totalUnits < 4:
            place = self.client.place()
            if place:
                self.placeCost += 10
                print(self.placeCost)

            next = False
            return None


        if self.attackUnit1Data["unit lvl"] < 3 and next:
            t = self.client.upgradeUnit(self.attackUnit1)
            if t:
                self.attackUnit1Data["unit lvl"] += 1
            next = False
            return None

        if self.supportAttackUnit1Data["ammount units"] < 2 and next:
            place = self.client.place()
            if place:
                self.placeCost += 10
                print(self.placeCost)
            next = False
            return None

        if self.supportAttackUnit1Data["unit lvl"] < 3 and next:
            t = self.client.upgradeUnit(self.supportAttackUnit1)
            if t:
                self.supportAttackUnit1Data["unit lvl"] += 1
            next = False
            return None

        if next:
            place = self.client.place()
            if place:
                self.placeCost += 10
                print(self.placeCost)
            next = False
            return None




    def merge(self):
        if len(self.attackUnit2Data["locations"]) >= 2 and self.attackUnit1Data["ammount units"] >= 2:
            mergeFrom = self.attackUnit2Data["locations"][0]
            mergeTo = self.attackUnit2Data["locations"][1]

            mergeFrom = self.fieldLocation[mergeFrom[0]][mergeFrom[1]]
            mergeTo = self.fieldLocation[mergeTo[0]][mergeTo[1]]

            self.client.mergeUnits(mergeFrom, mergeTo)


        if len(self.supportAttackUnit2Data["locations"]) >= 2:
            mergeFrom = self.supportAttackUnit2Data["locations"][0]
            mergeTo = self.supportAttackUnit2Data["locations"][1]

            mergeFrom = self.fieldLocation[mergeFrom[0]][mergeFrom[1]]
            mergeTo = self.fieldLocation[mergeTo[0]][mergeTo[1]]

            self.client.mergeUnits(mergeFrom, mergeTo)

        if len(self.supportUnit1Data["locations"]) >= 2:
            mergeFrom = self.supportUnit1Data["locations"][0]
            mergeTo = self.supportUnit1Data["locations"][1]

            mergeFrom = self.fieldLocation[mergeFrom[0]][mergeFrom[1]]
            mergeTo = self.fieldLocation[mergeTo[0]][mergeTo[1]]

            self.client.mergeUnits(mergeFrom, mergeTo)

        if len(self.supportAttackUnit2Data["locations"]) >= 4:
            mergeFrom = self.supportAttackUnit2Data["locations"][0]
            mergeTo = self.supportAttackUnit2Data["locations"][1]

            mergeFrom = self.fieldLocation[mergeFrom[0]][mergeFrom[1]]
            mergeTo = self.fieldLocation[mergeTo[0]][mergeTo[1]]

            self.client.mergeUnits(mergeFrom, mergeTo)


