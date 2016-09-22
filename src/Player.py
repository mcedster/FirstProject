import random

class player:
    def __init__(self, role):
        if role == "warrior":
            self.max_health = 30
            self.health = self.max_health
            self.max_mana = 20
            self.mana = self.max_mana
            self.inventory = []
            self.weapon = None
            self.armor = 6
            self.magic_resist = 2
            self.speed = 2
            self.level = 1
            self.ability = ["shield bolster", "enrage", "double-slash"]
            self.gold = 0
        if role == "mage":
            self.max_health = 20
            self.health = self.max_health
            self.max_mana = 50
            self.mana = self.max_mana
            self.inventory = []
            self.weapon = None
            self.armor = 2
            self.magic_resist = 5
            self.speed = 3
            self.level = 1
            self.ability = ["fireball", "icicle", "lightning", "earth shock"]
            self.gold = 0
        if role == "archer":
            self.max_health = 25
            self.health = self.max_health
            self.max_mana = 30
            self.mana = self.max_mana
            self.inventory = []
            self.weapon = None
            self.armor = 4
            self.magic_resist = 3
            self.speed = 4
            self.level = 1
            self.ability = ["hawk-eye", "triple shot", "double team"]
            self.gold = 0