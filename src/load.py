# Made by NexusMenace

# Class Data
classes = []
damage = []
health = []

# Enemy Data
enemies = []
edmg = []
ehp = []

def loadClasses(): # Loads data from data/classes.stat
    with open("src/data/classes.stat", "r") as file:
        for line in file:
            name, dmg, hp = line.strip().split(":")
            classes.append(name)
            damage.append(dmg)
            health.append(hp)

def loadEnemies(): # loads data from data/enemy.stat
    with open("src/data/enemy.stat", "r") as file:
        for line in file:
            name, dmg, hp = line.strip().split(":")
            enemies.append(name)
            edmg.append(dmg)
            ehp.append(hp)