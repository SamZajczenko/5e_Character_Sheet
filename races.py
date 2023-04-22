import math
import random
from tabulate import tabulate
from random import randint
from character import *
from dice import *
from classes import *
from dictionaries import *

# Random values and lists that are helful. 
languages_main = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic"]

# Probability of list being chosen
languages_probabilities = (random.choices(languages_main, weights=(20, 10, 10, 5, 10, 10, 10, 5, 5, 5, 10), k=other))

# This is to choose a what abilty scores you would like to increase.
def race_mod():
    if race == races[0]:
        
    elif race == races[1]:
        
    elif race == races[2]:
        
    elif race == races[3]:
        
    elif race == races[4]:
        
    elif race == races[5]:
        
    elif race == races[6]:
        
    elif race == races[7]:
        
    elif race == races[8]:

def score_increase():
    print(tabulate(scores, classesfmt = 'fancy_grid'))
    amount = 
    which = print(input(f'What scores would you like to increase, you may choose {amount}. Choose from the list above. '))
    if which.contains(strength):
        
    elif which.contains(dexterity):

    elif which.contains(constitution):
        
    elif which.contains(intelligence):
        
    elif which.contains(wisdom):
        
    elif which.contains(charisma):
        
    else:
        return None

# The races of dnd. I am going to have a main function and then subdivisions.
races = [["dwarf"],["elf"],["halfling"],["human"],["dragonborn"],["gnome"],["half_elf"],["half_orc"],["tiefling"]]

class Race:
    def __init__(self, speed, score, darkvision, abilities, language):
        self.speed = speed
        self.score = score
        self.darkvision = darkvision
        self.abilities = abilities
        self.language = language

# Dwarven race.
class Dwarf(Race):
    def __init__(self, hill=False, mountain=False):
        abilities = ["darkvision", "dwarven resilience", "stonecunning"]
        if hill:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven toughness")
        elif mountain:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven armor training")
        else:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
    
# Elven race.
class Elf(Race):
    def __init__(self, wood=False, drow=False, high=False):
        abilities = ["darkvision", "keen sense", "fey ancestry", "trance"]
        if wood:
            super().__init__(speed=35, score=[0,2,0,0,1,0], darkvision=True, abilities=abilities, language="Common, Elvish")
            self.abilities.append("mask of the wild","elf weapon training")
        elif drow:
            super().__init__(speed=30, score=[0,2,0,0,0,1], darkvision=True, abilities=abilities, language="Common, Elvish")
            self.abilities.append("elf weapon training", "cantrip")
        elif high:
            super().__init__(speed=30, score=[0,2,0,1,0,0], darkvision=False, abilities=abilities, language="Common, Elvish")
            self.abilities.append("superior darkvision", "sunlight sensitivity", "drow magic", "drow weapon casting")
        else:
            super().__init__(speed=30, score=[0,2,0,0,0,0], darkvision=False, abilities=abilities, language="Common, Elvish")

class Halfling(Race):
    def __init__(self, lightfoot=False, stout=False):
        abilities = ["lucky", "halfling nimbleness", "brave"]
        if lightfoot:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")
            self.abilities.append("naturally stealthy")
        elif stout:
            super().__init__(speed=25, score=[0, 2, 1, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")
            self.abilities.append("stout resilience")
        else:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")

class Human(Race):
    def __init__(self, variant=False):
        abilities = []
        if variant:
            super().__init__(speed=30, score=[1, 1, 1, 1, 1, 1], darkvision=False, abilities=abilities, languages="Common")
        else:
            super().__init__(speed=30, score=[0, 0, 0, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common")

class Dragonborn(Race):
    def __init__(self, score):
        abilities = ["draconic ancestry", "breath weapon"]
        super().__init__(speed=30, score=score, darkvision=False, abilities=abilities, languages="Common, Draconic")

class Gnome(Race):
    def __init__(self, forest=False, rock=False):
        abilities = ["gnome cunning"]
        if forest:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 1], darkvision=True, abilities=abilities, languages="Common, Gnomish")
            self.abilities.append("natural illusionist")
        elif rock:
            super().__init__(speed=25, score=[0, 2, 1, 0, 0, 0], darkvision=True, abilities=abilities, languages="Common, Gnomish")
            self.abilities.append("artificer's lore")
        else:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 0], darkvision=True, abilities=abilities, languages="Common, Gnomish")

class Half_elf(Race):
    def __init__(self, score):
        abilities = ["darkvision", "fey ancestry", "skill versatility"]
        super().__init__(speed=30, score=score, darkvision=True, abilities=abilities, languages="Common, Elvish")

class Half_orc(Race):
    def __init__(self, score):
        abilities = ["darkvision", "menacing", "relentless endurance", "savage attacks"]
        super().__init__(speed=30, score=score, darkvision=True, abilities=abilities, languages="Common, Orcish")

class Tiefling(Race):
    def __init__(self, speed=30, score=[0, 0, 0, 1, 0, 2], darkvision=True, abilities=["hellish resistance", "infernal legacy"], language="Common, Infernal"):
        super().__init__(speed, score, darkvision, abilities, language)
