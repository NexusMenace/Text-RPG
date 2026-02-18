# Made by NexusMenace

from src import load

def settings():
    print("Please choose difficulty scale. (0.5 - 3.0)")
    while True:
        diff_str = input("> ").strip()
        try:
            diff_str = float(diff_str)
        except ValueError:
            print("[Error] Please input a number like 1.0")
            continue
        if 0.5 <= diff_str <= 3.0:
            print(f"Difficulty set to {diff_str}")
            return diff_str
        else:
            print("Out of range — enter a value between 0.5 and 3.0")
            continue

def selectClass():
    print("Please select your class.")
    print("Type 'list' to list available classes.")
    print("Type 'stat' to list classes HP and DMG.")
    while True:
        classInp = input("> ")
        if classInp == "list":
            for i in load.classes:
                print(i)
        elif classInp == 'stat':
            it = 0
            for i in load.classes:
                print(f"{i}:")
                print(f"HP: {str(load.health[it])}")
                print(f"DMG: {str(load.damage[it])}")
                print()
                it += 1
        elif classInp in load.classes:
            print(f"{classInp} class selected.")
            return classInp

def gameLoop(user, diff):
    while True:
        print("Type 'end' to end game.")
        inp = input("> ")
        if inp == "end":
            break
    print("Game Over!")

class Player:
    def __init__(self, MaxHP, dmg):
        self.hp = int(MaxHP)
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
    
    def HarmPlayer(self, val):
        self.hp -= val

def runGame():
    diff = settings()
    userClass = selectClass()
    ind = load.classes.index(userClass)
    user = Player(load.health[ind], load.damage[ind])
    gameLoop(user, diff)
