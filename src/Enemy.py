import random

class enemy:
    def __init__(self, name):
        if name == "imp":
            self.health = 10
            self.armor = 0
            self.magic_resist = 0
            self.item = 0
            self.weapon = None
            self.speed = 1
            self.level = 0
            self.exp = 3
            self.gold = 5
        if name == "slime":
            self.health = 18
            self.armor = 3
            self.magic_resist = 1
            self.item = 0
            self.weapon = None
            self.speed = 2
            self.level = 1
            self.exp = 5
            self.gold = 8
        if name == "skeleton":
            self.health = 25
            self.armor = 3
            self.magic_resist = 2
            self.item = 0 #after u know how many items u gonna have, put the random int thing here
            self.weapon = None
            self.speed = 3
            self.level = 3
            self.exp = 8
            self.gold = 12
        if name == "basilisk":

        if name == "lizard-man":
        if name == "minotaur":
        if name == "vampire-bat":


        if name == "Mighty-Grey": # boss
            self.status = 0  #0 is normal, 1 is burned, 2 is paralyzed (might be hard to code), 3 is poisoned,



