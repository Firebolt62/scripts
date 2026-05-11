import random
import time
from dataclasses import dataclass

@dataclass
class Enemy:
    name: str
    health: int
    abilities: list

@dataclass
class Character:
    name: str
    health: int
    abilities: list

enemies = [
    Enemy("Blastoise", 100,
          [ "Root Bind"
          , "Mind Shatter"
          , "Future Sight Echo"
          , "Telekinetic Crush"
          ])
    ,
    Enemy("Thundercat", 100,
          [ "Vine Dominion"
          , "Spore Mist"
          , "Nature's Renewal"
          , "Thorn Burst"
          ])
    ,
    Enemy("Magicarp", 100,
          [ "Thunder Call"
          , "Cloud Step"
          , "Pressure Crush"
          , "Sky Splitter"
          ])
    ,
    Enemy("Mewtwo", 100,
          [ "Terra Break"
          , "Frost Bloom"
          , "Sandstorm Veil"
          , "Magma Armor"
          ])
]

characters = [

    #TODO: add more characters
    
    Character("Firebolt", 100,
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

    #TODO: make abilities have specific damage instead of random damage and add a critical hit chance and limited uses for each ability

    damage_dealt = int(random.randint(10,35) / difficulty)
    enemy.health -= damage_dealt
    return damage_dealt

def enemy_attack(enemy, character):
    ability = random.choice(enemy.abilities)
    damage_dealt = random.randint(10,35)
    character.health -= damage_dealt
    return (damage_dealt, ability)

def main():
    num_rounds = 0
    difficulty = 1.0
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
                num_rounds += 1
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
                print(f"You were defeated by {enemy.name}! You lasted {num_rounds} rounds.")
                num_rounds = 0
                time.sleep(0.7) 
                print()
                quit_option = input("Do you want to try again? (y/n): ").lower()
                if quit_option != 'y':
                    print("Thanks for playing!")
                    break

                print("Next enemy approaches...")
                time.sleep(2)
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