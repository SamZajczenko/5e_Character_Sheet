from tabulate import tabulate
import math
from races import *
from probabilities import *

classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
races = ["dwarf","elf","halfling","human","dragonborn","gnome","half_elf","half_orc","tiefling"]
scores = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

# Level then bonus. 
table_prof_bonus = [0-4, 2],[5-8, 3],[9-12, 4],[13-16, 5],[17-20, 6] 

def races():
  print(tabulate(races, racesfmt = 'fancy_grid'))

def char_classes():
  print(tabulate(classes, classesfmt = 'fancy_grid'))

modifiers = [(-5, i) if i == 0 else ((i - 1) // 2 - 5, i) for i in range(31)]

def passive_wis(wisdom, modifiers):
  i = wisdom
  passive_wisdom = 10 + modifiers(i) 
  return passive_wisdom  

# Dungeons and Dragons classes code
class Class_Main:
    def __init__(self, armor_class):
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.weapons = weapons
        self.all_prof = all_prof
        self.personality = personality
        self.weapons = weapons
        self.equipment = equipment
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.features_traits = features_traits
        self.spells = spells
        self.spell_save_DC = spell_save_DC
        self.spell_attack_bonus = spell_attack_bonus
        self.money = 0

   
    
    def armor():
        armors = [
            ["light armor", ["padded",5]["leather",10]["studded leather",45]],
            ["medium armor", ["hide", 10]["chain shirt", 50]["scale mail", 50]["breastplate", 400]["half plate", 750]],
            ["heavy armor",["ring mail", 30]["chain mail", 75]["splint", 17]["plate", 18]]
            ]
        armors_display = [
            ["light armor", ["padded",5]["leather",10]["studded leather",45]],
            ["medium armor", ["hide", 10]["chain shirt", 50]["scale mail", 50]["breastplate", 400]["half plate", 750]],
            ["heavy armor",["ring mail", 30]["chain mail", 75]["splint", 17]["plate", 18]]
            ]
        # Sheild, money, and bonus onto AC
        sheild = [sheild, 10, 2]
        print(tabulate(armors_display, armors_displayfmt = 'fancy_grid'))
        choice = input("What armor would you like to use? ")
        if choice == armors[]:
            if money == armors[]:
                value = armor_class[]
                money -= value
                armor_class = armors[]
            else:
                print("")
        elif choice == armors[]:
            if money == armors[]:
                value = armor_class[]
                money -= value
                armor_class = armors[]
            else:
                print("")
            
        else:
            None
        
        if choice == armors[0][0 or 1][0]:
        
        elif choice == armors[0][2][0]:
            
            
class Barbarian(Class_Main):
    def __init__(self, ):