# Made by NexusMenace

class Player: # Player Class, functions for easier management
    def __init__(self, hp, dmg):
        self.maxhp = int(hp)
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.gold = 0
        self.kills = 0
    
    def isAlive(self):
        if self.hp > 0:
            return True
        else:
            return False
    
    def setHP(self, val):
        self.hp = val
    
    def HealPlayer(self, val):
        self.hp += val
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def HarmPlayer(self, val):
        self.hp -= val