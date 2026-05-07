import random
import time
from dataclasses import dataclass
'''
===============================
YPC 2026 - Battle Game
Developed by: Adnan Poonawala
===============================
'''
@dataclass
class Enemy:
    name: str
    health: int
    class_type: str
    abilities: list

@dataclass
class Character:
    name: str
    health: int
    class_type: str
    abilities: list

enemies = [
    Enemy("Blastoise", 100, None,
          [ "Root Bind"
          , "Mind Shatter"
          , "Future Sight Echo"
          , "Telekinetic Crush"
          ])
    ,
    Enemy("Thundercat", 100, None,
          [ "Vine Dominion"
          , "Spore Mist"
          , "Nature's Renewal"
          , "Thorn Burst"
          ])
    ,
    Enemy("Magicarp", 100, None,
          [ "Thunder Call"
          , "Cloud Step"
          , "Pressure Crush"
          , "Sky Splitter"
          ])
    ,
    Enemy("Mewtwo", 100, None,
          [ "Terra Break"
          , "Frost Bloom"
          , "Sandstorm Veil"
          , "Magma Armor"
          ])
]

characters = [
    Character("Firebolt", 100, "Lightning",
              [ "Flame Whip"
              , "Ground Thrash"
              , "Thunderslash"
              , "Waterwheel"
              , "Charge and Blast"
              ])
    ]

def reset_game(character):
    
    enemy = random.choice(enemies)
    enemy.health = 100
    character.health = 100
    print()
    print(f"A wild {enemy.name} appears!\n")

    return enemy
 
def player_attack(enemy, difficulty):
    damage_dealt = int(random.randint(10,35) / (1.0 * difficulty))
    enemy.health-= damage_dealt
    return damage_dealt

def enemy_attack(enemy, character):
    ability = random.choice(enemy.abilities)
    damage_dealt = random.randint(10,35)
    character.health -= damage_dealt
    return (damage_dealt, ability)

def main():
    difficulty = 1
    damage_dealt = 0
    character = characters[0]
    enemy = reset_game(character)

    while enemy.health > 0 and character.health > 0:

        for i, ability in enumerate(character.abilities, 1):
            print(f"{i}. {ability}")

        choice = -1

        try:
            print()
            choice = int(input("choose your ability number: ")) - 1
        except ValueError:
            pass

        print()   
        if choice >= 0 and choice < len(character.abilities):
            time.sleep(0.7)
            print(f"You used {character.abilities[choice]}!")
            damage_dealt = player_attack(enemy, difficulty)
            time.sleep(0.7)
            print(f"You dealt {damage_dealt}% damage!")
            time.sleep(0.7)
            if enemy.health <= 0:
                print(f"You defeated {enemy.name}!")
                time.sleep(0.7) 
                print()
                print("Next enemy approaches...")
                time.sleep(2)
                difficulty *= 1.2
                enemy = reset_game(character)
                continue

            print(f"{enemy.name} now has {enemy.health}% health!")
            print()
            
            damage_dealt, ability = enemy_attack(enemy, character)
            time.sleep(1.5)
            print(f"{enemy.name} used {ability}!")
            time.sleep(0.7)
            print(f"{enemy.name} dealt {damage_dealt}% damage!")
            time.sleep(0.7)
            if character.health <= 0:
                print(f"You were defeated by {enemy.name}!")
                time.sleep(0.7) 
                print()
                print("Next enemy approaches...")
                time.sleep(2)
                difficulty *= 1.2
                enemy = reset_game(character)
                continue

            print(f"You now have {character.health}% health!")
            print()
            time.sleep(0.7)
        else:
            print(f"Please choose an option from 1 - {len(character.abilities)}")
            print()

if __name__ == "__main__":
    main()