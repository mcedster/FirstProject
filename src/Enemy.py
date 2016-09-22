import random

class enemy:
    def __init__(self, name):
        if name == "imp":
            self.max_health = 10
            self.health = self.max_health
            self.attack = 0
            self.armor = 0
            self.magic_resist = 0
            self.item = 0
            self.weapon = None #TODO have it state what item it has
            self.speed = 1
            self.level = 0
            self.exp = 3
            self.gold = 5
        if name == "slime":
            self.max_health = 18
            self.health = self.max_health
            self.attack = 0 # cahnge
            self.armor = 3
            self.magic_resist = 1
            self.item = 0
            self.weapon = None
            self.speed = 2
            self.level = 1
            self.exp = 5
            self.gold = 8
        if name == "skeleton":
            self.max_health = 25
            self.health = self.max_health
            self.attack = 0
            self.armor = 3
            self.magic_resist = 2
            self.item = 0 #after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 3
            self.level = 3
            self.exp = 8
            self.gold = 12
        if name == "vampire-bat":
            self.max_health = 30
            self.health = self.max_health
            self.attack = 0
            self.armor = 3
            self.magic_resist = 2
            self.item = 0  # after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 3
            self.level = 3
            self.exp = 10
            self.gold = 14
        if name == "basilisk":
            self.max_health = 40
            self.health = self.max_health
            self.attack = 0
            self.armor = 5
            self.magic_resist = 5
            self.item = 0  # after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 5
            self.level = 5
            self.exp = 18
            self.gold = 20
        if name == "lizard-man":
            self.max_health = 50
            self.health = self.max_health
            self.attack = 0
            self.armor = 6
            self.magic_resist = 5
            self.item = 0  # after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 5
            self.level = 6
            self.exp = 24
            self.gold = 28
        if name == "minotaur":
            self.max_health = 70
            self.health = self.max_health
            self.attack = 0
            self.armor = 7
            self.magic_resist = 5
            self.item = 0  # after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 6
            self.level = 7
            self.exp = 29
            self.gold = 40
        if name == "Fusion":
            self.max_health = 100
            self.health = self.max_health
            self.attack = 0
            self.armor = 10
            self.magic_resist = 10
            self.item = 0  # after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 10
            self.level = 10
            self.exp = 50
            self.gold = 100
        if name == "Jeremy":
            self.gold = -50



        if name == "Mighty-Grey": # boss
            self.status = 0  #0 is normal, 1 is burned, 2 is paralyzed (might be hard to code), 3 is poisoned,


