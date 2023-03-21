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
class Dwarf(Race):
    def __init__(self, hill=False, mountain=False):
        abilities = ["darkvision", "dwarven resilience", "stonecunning"]
        if hill:
            super().__init__(speed=25, score=[2, 0, 2, 0, 0, -2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven toughness")
        elif mountain:
            super().__init__(speed=25, score=[2, 0, 2, 0, 0, -2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven armor training")
        else:
            super().__init__(speed=25, score=[2, 0, 2, 0, 0, -2], darkvision=True, abilities=abilities, language="Common, Dwarvish")

    dwarf_dict = {
        "dwarf_abilities": ["darkvision", "dwarven resilience", "stonecunning"],
        "hill_dwarf_abilities": ["darkvision", "dwarven resilience", "stonecunning", "dwarven toughness"],
        "mountain_dwarf_abilities": ["darkvision", "dwarven resilience", "stonecunning", "dwarven armor training"],
    }

    dwarf_abilities = ""
        

# Elven race.
class Elf(Race):
    def __init__(self, wood=False, drow=False, high=False):
        if wood:
            super().__init__(speed=35, score=[0,2,0,0,1,0], darkvision=True, abilities="", language="Common, Elvish")
        elif drow:
            super().__init__(speed=30, score=[0,2,0,0,0,1], darkvision=True, abilities="", language="Common, Elvish")
        elif high:
            super().__init__(speed=30, score=[0,2,0,1,0,0], darkvision=False, abilities="", language="Common, Elvish")
        else:
            super().__init__(speed=30, score=[0,2,0,0,0,0], darkvision=False, abilities="", language="Common, Elvish")
    
    elf_dict = {
        "elf_abilities": ["darkvision", "keen sense", "fey ancestry", "trance"],
        "wood_elf_abilities": ["mask of the wild", "elf weapon training"],
        "high_elf_abilities": ["elf weapon training","cantrip"],
        "drow_elf_abilities": ["superior darkvision", "sunlight sensitivity", "drow magic", "drow weapon casting"],
    }

    elf_abilities = ""


# Halfling race.
class Halfling(Race):
    def __init__(self, lightfoot=False, stout=False):
        if lightfoot:   
            super().__init__(speed=25, score=[0,2,0,0,0,0], darkvision=False, abilities=abilities, language="Common, Halfling") 
        if stout:
            super().__init__(speed=25, score=[0,2,0,0,0,0], darkvision=False, abilities=abilities, language="Common, Halfling") 
        else:
            super().__init__(speed=25, score=[0,2,0,0,0,0], darkvision=False, abilities=abilities, language="Common, Halfling") 
    
    halfling_dict = {
        "halfling_abilities": ["lucky"],
        "lightfoot_halfling_abilities": , 
        "stout_halfling_abilities": , 
    }

    halfling_abilities = ""


# Human race.
class Human(Race):
  def __init__(self):
      super().__init__(speed, score, darkvision, abilities, language)

    human_dict = {
        "human_abilities": "",
    }
        
    human_abilities = ""

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