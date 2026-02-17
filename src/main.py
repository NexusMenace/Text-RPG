# Made by NexusMenace

def settings():
    print("Please choose difficulty scale. (0.5 - 3.0)")
    while True:
        diff_str = input("> ").strip()
        try:
            diff = float(diff_str)
        except ValueError:
            print("[Error] Please input a number like 1.0")
            continue
        if 0.5 <= diff <= 3.0:
            print(f"Difficulty set to {diff}")
            runGame(diff)
            return
        else:
            print("Out of range — enter a value between 0.5 and 3.0")
            continue

def runGame(difficulty=1.0):
    pass