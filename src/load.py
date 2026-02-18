# Made by NexusMenace

classes = []
damage = []
health = []

def loadClasses():
    with open("src/data/classes.stat", "r") as file:
        for line in file:
            name, dmg, hp = line.strip().split(":")
            classes.append(name)
            damage.append(dmg)
            health.append(hp)