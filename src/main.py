# Made by NexusMenace

# Imports
from src import load # Imports functions and data from load.py
from src import player as plr # Imports Player Class from player.py
from random import randint

def settings(): # Allows the player to select difficulty scale.
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

def selectClass(): # Class selection function
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

def gameLoop(user, diff): # Main game loop function
    print("Type 'end' to end game.")
    print("Type 'stat' to list player stats.")
    print("Type 'fight' to fight a random enemy.")
    print("Type 'rest' to heal 5-8 health.")

    commands = [
        "end",
        "stat",
        "fight",
        "rest"
    ]

    while True:
        inp = input("> ")
        if inp.lower() == "end":
            break
        if inp.lower() == "stat":
            print("Player Stats:")
            print(f"Health: {user.hp}")
            print(f"Damage: {user.dmg}")
            print(f"Gold: {user.gold}")
            print()
        if inp.lower() == "fight":
            print("Feature not implemented yet, sorry.")
        if inp.lower() == "rest":
            ham = randint(5, 8)
            user.HealPlayer(ham)
            print(f"You have been healed {ham} HP!")
        if not inp.lower() in commands:
            print(f"{inp} is not a command.")


def runGame(): # Main function, sets up variables for game
    diff = settings()
    userClass = selectClass()
    ind = load.classes.index(userClass)
    user = plr.Player(load.health[ind], load.damage[ind])

    gameLoop(user, diff)
    print("Game Over!")
