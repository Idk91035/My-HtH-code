# hero.py for hero profile
import random
from ability import Ability
from armor import Armor
class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities =[]
        self.armors = []

    def battle(self, opponent):
        winner = random.choice([self.name, opponent.name])
        print(f"{winner} wins the battle!")
    
    def add_ability(self, ability):
        self.abilities.append(ability)
        print(f"{ability.name} has been added to {self.name}")
    def sum_of_attacks(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s list")

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    

if __name__ =="__main__":
    my_hero = Hero("Grace Hopper",200)
    print(my_hero.name)
    print(my_hero.current_health)


    
    my_hero1 = Hero("ironMan",200)
    print(my_hero1.name)
    print(my_hero1.current_health)

    my_hero1.battle(my_hero)

    my_hero.add_ability(Ability("Fireball", 30))
    my_hero.add_ability(Ability("water", 40))
    my_hero.add_ability(Ability("ice", 20))
    my_hero.add_armor(Armor("sheild",50))
    my_hero.add_armor(Armor("iron helmet",20))
    my_hero.add_armor(Armor("iron chesplate",70))
    print(my_hero.sum_of_attacks())
    print(my_hero.defend())

# arena.py

from hero import Hero
from ability import Ability
from armor import Armor

def main():
    # Create some abilities
    fireball = Ability("Fireball", 50)
    lightning_strike = Ability("Lightning Strike", 70)

    # Create some armors
    shield = Armor("Shield", 30)
    armor_plate = Armor("Armor Plate", 40)

    # Create heroes
    hero1 = Hero("Grace Hopper", 200)
    hero2 = Hero("Alan Turing", 150)

    # Add abilities to heroes
    hero1.add_ability(fireball)
    hero1.add_ability(lightning_strike)
    
    hero2.add_ability(fireball)

    # Add armor to heroes
    hero1.add_armor(shield)
    hero2.add_armor(armor_plate)

    # Print initial stats
    print(f"{hero1.name} Health: {hero1.current_health}")
    print(f"{hero2.name} Health: {hero2.current_health}")

    # Hero1 attacks hero2
    hero1_attack = hero1.sum_of_attacks()
    print(f"{hero1.name} attacks with a total damage of {hero1_attack}")

    # Hero2 defends
    hero2_defense = hero2.defend()
    print(f"{hero2.name} defends with a total block of {hero2_defense}")

    # Print the final battle result
    final_damage = hero1_attack - hero2_defense
    hero2.current_health -= max(final_damage, 0)
    print(f"{hero2.name}'s Health after attack: {hero2.current_health}")

    # Determine the winner
    if hero2.current_health <= 0:
        print(f"{hero1.name} wins the battle!")
    else:
        print(f"{hero2.name} is still standing!")

    # Battle between two heroes (randomized winner)
    hero1.battle(hero2)

if __name__ == "__main__":
    main()
