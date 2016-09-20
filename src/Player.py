import random

class player:
    def __init__(self, role):
        if role == "warrior":
            self.health = 30
            self.mana = 10
            self.inventory = []
            self.weapon = None
            self.armor = 6
            self.magic_resist = 2
            self.speed = 2
            self.level = 1
            self.ability = ["shield bolster", "enrage", "double-slash"]
            self.gold = 0
        if role == "mage":
            self.health = 20
            self.mana = 25
            self.inventory = []
            self.weapon = None
            self.armor = 2
            self.magic_resist = 5
            self.speed = 3
            self.level = 1
            self.ability = ["fireball", "icicle", "lightning", "earth shock"]
            self.gold = 0
        if role == "archer":
            self.health = 25
            self.mana = 15
            self.inventory = []
            self.weapon = None
            self.armor = 4
            self.magic_resist = 3
            self.speed = 4
            self.level = 1
            self.ability = ["hawk-eye", "triple shot", "double team"]
            self.gold = 0