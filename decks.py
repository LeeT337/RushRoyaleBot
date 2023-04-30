import numpy as np


class Decks:
    def __init__(self, cards):
        self.cards = np.array(cards)
        print(self.cards)
        solutions = np.argwhere(self.cards == "Fire Mage")
        print(solutions)

        self.cardData = []
        for i in range(len(cards)):
            self.cardData.append(self.getCardData(cards[i]))


        print(self.cardData)


    def getCardData(self, card):
        match card[0]:
            case "Archer":
                damage = 29 + (3 * card[1])
                attackSpeedIncrease = 10 + (2 * card[1])
                morale = 1 + (0.2 * card[1])
                attackInterval = 0.45
                canUpgradePic = "./photos/ArcherCan.png"
                cantUpgradePic = "./photos/ArcherCant.png"
                locatePixel = "./photos/ArcherPixelColor.png"
                data = {
                    "name": "Archer",
                    "card lvl": 1,
                    "upgrade cost": 100,
                    "unit on field": 0,
                    "damage": damage,
                    "attack speed increase": attackSpeedIncrease,
                    "attack interval": attackInterval,
                    "morale": morale,
                    "can upgrade pic": canUpgradePic,
                    "cant upgrade pic": cantUpgradePic,
                    "damage per lvl": 23,
                    "attack speed increase per lvl": 10,
                    "locate pixel": locatePixel,
                    "locate color": (189, 251, 169)
                }
            case "Poisoner":
                damage = 13 + (5 * card[1])
                venomDamage = 12 + (5 * card[1])
                morale = 1 + (0.3 * card[1])
                attackInterval = 2.5 - (0.02 * card[1])
                canUpgradePic = "./photos/PoisonerCan.png"
                cantUpgradePic = "./photos/PoisonerCant.png"
                locatePixel = "./photos/PoisonerPixelColor.png"
                data = {
                    "name": "Poisoner",
                    "card lvl": 1,
                    "upgrade cost": 100,
                    "unit on field": 0,
                    "damage": damage,
                    "attack interval": attackInterval,
                    "venom damage": venomDamage,
                    "morale": morale,
                    "can upgrade pic": canUpgradePic,
                    "cant upgrade pic": cantUpgradePic,
                    "locate pixel": locatePixel,
                    "locate color": (60, 220, 49)
                }
            case "Fire Mage":
                damage = 27 + (3 * card[1])
                areaDamage = 12 + (3 * card[1])
                morale = 1 + (0.3 * card[1])
                attackInterval = 0.8 - (0.01 * card[1])
                canUpgradePic = "./photos/FireMageCan.png"
                cantUpgradePic = "./photos/FireMageCant.png"
                locatePixel = "./photos/FireMagePixelColor.png"
                data = {
                    "name": "Fire Mage",
                    "card lvl": 1,
                    "upgrade cost": 100,
                    "unit on field": 0,
                    "damage": damage,
                    "attack interval": attackInterval,
                    "area damage": areaDamage,
                    "morale": morale,
                    "can upgrade pic": canUpgradePic,
                    "cant upgrade pic": cantUpgradePic,
                    "locate pixel": locatePixel,
                    "locate color": (250, 173, 66)
                }
            case "Lightning Mage":
                damage = 26 + (3 * card[1])
                lightningDamage = 33 + (5 * card[1])
                morale = 1 + (0.3 * card[1])
                attackInterval = 0.7 - (0.02 * card[1])
                canUpgradePic = "./photos/LightingMageCan.png"
                cantUpgradePic = "./photos/LightingMageCant.png"
                locatePixel = "./photos/LightingMagePixelColor.png"
                data = {
                    "name": "Lightning Mage",
                    "card lvl": 1,
                    "upgrade cost": 100,
                    "unit on field": 0,
                    "damage": damage,
                    "attack interval": attackInterval,
                    "lightning damage": lightningDamage,
                    "morale": morale,
                    "can upgrade pic": canUpgradePic,
                    "cant upgrade pic": cantUpgradePic,
                    "locate pixel": locatePixel,
                    "locate color": (254, 255, 133)
                }
            case "Cold Mage":
                damage = 15 + (2 * card[1])
                slowTarget = 5 + (0.5 * card[1])
                morale = 1 + (0.3 * card[1])
                attackInterval = 1.5 - (0.02 * card[1])
                canUpgradePic = "./photos/ColdMageCan.png"
                cantUpgradePic = "./photos/ColdMageCant.png"
                locatePixel = "./photos/ColdMagePixelColor.png"
                data = {
                    "name": "Cold Mage",
                    "card lvl": 1,
                    "upgrade cost": 100,
                    "unit on field": 0,
                    "damage": damage,
                    "attack interval": attackInterval,
                    "slow target": slowTarget,
                    "morale": morale,
                    "can upgrade pic": canUpgradePic,
                    "cant upgrade pic": cantUpgradePic,
                    "locate pixel": locatePixel,
                    "locate color": (165, 249, 246)
                }
            case _:
                data = {
                    "damage": 0
                }


        return data

