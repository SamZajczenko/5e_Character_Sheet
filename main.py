import math
import random
from random import randint

# These will be the dice the character will use. 
def roll(num, dice):
  if num in dice:
    num=num.replace('d','')
    num = randint(1,int(num))
    print("You rolled a: " + str(num))
  else:
    print("That is not a valid number, pick a valid number")

# variables that should be tracked
class main_sheet():
  def one(self, alignment, age, ):
    self.alignment

class race:
  
  import math
from random import randint

def roll(num):
    if num.startswith('d'):
        num = randint(1, int(num[1:]))
        print(f"You rolled a {num}.")
    else:
        print("That is not a valid number, pick a valid number.")

class Race:
    def __init__(self, speed, score, darkvision, abilities, language):
        self.speed = speed
        self.score = score
        self.darkvision = darkvision
        self.abilities = abilities
        self.language = language

class elf(Race):
    def __init__(self, wood=False, drow=False, high=False):
        if wood:
            super().__init__(speed=35, score=2, darkvision=True, abilities="", language="Common, Elvish")
        elif drow:
            super().__init__(speed=30, score=2, darkvision=True, abilities="", language="Common, Elvish")
        elif high:
            super().__init__(speed=30, score=2, darkvision=False, abilities="", language="Common, Elvish")

class dwarf(Race):
    def __init__(self, hill=False, mountain=False):
        if hill:
            super().__init__(speed=25, score=2, darkvision=True, abilities="", language="Common, Dwarvish")
        elif mountain

class halfling(Race):
  def __init__(self, speed, score, darkvision, abilities, language):
     super().__init__(speed, score, darkvision, abilities, language) 

class human(Race):
  def

class dragonborn(Race):
  def

class gnome(Race):
  def

class halfelf(Race):
  def

class halforc(Race):
  def 

class tiefling(Race):
  def
  
class Character:
    def character(self, name, race, char_class, level, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print(f"Level: {self.level}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}")

# Sample character
character = Character("Gandalf", "Human", "Wizard", 10, 8, 14, 12, 18, 16, 20)

# Show character stats
character.show_stats()

class Items:
  def items(self, armor, ):
    self.armor = armor 