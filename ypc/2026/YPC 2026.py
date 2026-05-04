import random
import time

enemies = [
    "Blastoise",
    "Thundercat",
    "Magicarp",
    "Mewtwo"]

enemyAbilities = [
    "Inferno Pulse",
    "Tidal Grasp",
    "Volt Surge",
    "Terra Break",
    "Frost Bloom",
    "Sandstorm Veil",
    "Magma Armor",
    "Cyclone Dash",
    "Thunder Call",
    "Cloud Step",
    "Pressure Crush",
    "Sky Splitter",
    "Vine Dominion",
    "Spore Mist",
    "Nature's Renewal",
    "Thorn Burst",
    "Root Bind",
    "Mind Shatter",
    "Future Sight Echo",
    "Telekinetic Crush"]

character = {
    "name":"Firebolt",
    "health":100,
    "class":"Lightning",
    "abilities": [
        "Flame Whip",
        "Ground Thrash",
        "Thunderslash",
        "Waterwheel",
        "Charge and Blast"]
}

name = random.choice(enemies)
enemyChoice = random.choice(enemyAbilities)

enemy = {"name":name,
         "health":100,
         "abilities":enemyAbilities,}

def reset_game():
    global enemy, name, enemyChoice
    
    name = random.choice(enemies)
    enemyChoice = random.choice(enemyAbilities)

    enemy = {
        "name": name,
        "health": 100,
        "abilities": enemyAbilities
    }

    character["health"] = 100
    print()
    print(f"A wild {enemy['name']} appears!\n")
    
def playerAttack():
    global DamageDealt
    DamageDealt = random.randint(10,35)
    enemy["health"]-= DamageDealt

def enemyAttack():
    global enemyChoice
    global DamageDealt
    ability = random.choice(enemy["abilities"])
    enemyChoice = ability
    DamageDealt = random.randint(10,35)
    character["health"]-= DamageDealt

reset_game()

while enemy["health"] > 0 and character["health"] > 0:

    for i, ability in enumerate(character["abilities"], 1):
        print(f"{i}. {ability}")

    choice = -1

    try:
        print()
        choice = int(input("choose your ability number: ")) - 1
    except ValueError:
        pass

    print()   
    if choice >= 0 and choice < len(character["abilities"]):
        time.sleep(0.7)
        print(f"You used {character["abilities"][choice]}!")
        playerAttack()
        time.sleep(0.7)
        print(f"You dealt {DamageDealt} damage!")
        time.sleep(0.7)
        if enemy["health"] <= 0:
            print(f"You defeated {enemy['name']}!")
            time.sleep(0.7) 
            print()
            print("Next enemy approaches...")
            time.sleep(2)
            reset_game()
            continue
        else:
            pass
        print(f"{enemy["name"]} now has {enemy['health']} health!")
        print()
        enemyAttack()
        time.sleep(1.5)
        print(f"{enemy['name']} used {enemyChoice}!")
        time.sleep(0.7)
        print(f"{enemy['name']} dealt {DamageDealt} damage!")
        time.sleep(0.7)
        if character["health"] <= 0:
            print(f"You were defeated by {enemy['name']}!")
            time.sleep(0.7) 
            print()
            print("Next enemy approaches...")
            time.sleep(2)
            reset_game()
            continue
        else:
            pass
        print(f"You now have {character['health']} health!")
        print()
        time.sleep(0.7)
    else:
        print(f"Please choose an option from 1 - {len(character['abilities'])}")
        print()