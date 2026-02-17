# Made by NexusMenace

classes = []
damage = []
health = []

with open("src/data/classes.stat", "r") as file:
    for line in file:
        name, atk, hp = line.strip().split(":")

def loadClasses():
    with open("src/data/classes.stat", "r") as file:
        for line in file:
            name, dmg, hp = line.strip().split(":")
            classes.append(name)
            damage.append(dmg)
            health.append(hp)

print(classes)