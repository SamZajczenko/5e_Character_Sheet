import math
import random
from random import randint
from main import *
from dictionaries import * 

# Random values and lists that are helful. 
languages_main = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic"]

# Probability of list being chosen
other = ""
languages_probabilities = (random.choices(languages_main, weights=(20, 10, 10, 5, 10, 10, 10, 5, 5, 5, 10), k=other))


# The races of dnd. I am going to have a main function and then subdivisions.
score = []
abilties = [["dwarf"],["elf"],["halfling"],["human"],["dragonborn"],["gnome"],["half_elf"],["half_orc"],["tiefling"]]

class Race:
    def __init__(self, speed, score, darkvision, abilities, language):
        self.speed = speed
        self.score = score
        self.darkvision = darkvision
        self.abilities = abilities
        self.language = language


# Dwarven race.
class dwarf(Race):
    def __init__(self, hill=False, mountain=False):
        if hill:
            super().__init__(speed=25, score=[wisdom,1], darkvision=True, abilities=abilties[0][0], language="Common, Dwarvish")
        elif mountain:
            super().__init__(speed=25, score=[strength,2], darkvision=True, abilities=abilties[0][0], language="Common, Dwarvish")  
    
    dwarf_dict = {
        "dwarf_abilities": "",
        "hill_dwarf_abilities": "",
        "mountain_dwarf_abilities": "",
        }

    dwarf_abilities = ""
        

# Elven race.
class elf(Race):
    def __init__(self, wood=False, drow=False, high=False):
        if wood:
            super().__init__(speed=35, score=2, darkvision=True, abilities="", language="Common, Elvish")
        elif drow:
            super().__init__(speed=30, score=2, darkvision=True, abilities="", language="Common, Elvish")
        elif high:
            super().__init__(speed=30, score=2, darkvision=False, abilities="", language="Common, Elvish")
    elf_dict = {
        "elf_abilities": ""
        "wood_elf_abilities": "",
        "high_elf_abilities": "",
        "drow_elf_abilities": "",
        }

    elf_abilities = ""


# Halfling race.
class halfling(Race):
    def __init__()
    
halfling_dict = {
    "halfling_abilities": "",
}

halfling_abilities = ""

class halfling(Race):
  def __init__(self, speed, score, darkvision, abilities, language):
     super().__init__(speed, score, darkvision, abilities, language) 


# Human race.
class human(Race):
  def __init__()

# Dragonborn race.
class dragonborn(Race):
  
# Gnome race.
class gnome(Race):
  def __init__():

class half_elf(Race):
  def __init__():

class half_orc(Race):
  def __init__(): 

class tiefling(Race):
  def __init__():