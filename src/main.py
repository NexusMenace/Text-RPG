# Made by NexusMenace

def settings():
    print("Please choose difficulty. 0-1.0")
    while True:
        diff = input("> ")
        if diff == type(int):
            exit
        else:
            continue
    runGame()

def runGame():
    tmp = ""