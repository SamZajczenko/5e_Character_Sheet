import math
from random import randint
from races import *
from classes import *
from dictionaries import * 

# main document for all code

# # These will be the dice the character will use. 
# def roll(num, dice):
#   if num in dice:
#     num=num.replace('d','')
#     num = randint(1,int(num))
#     print("You rolled a: " + str(num))
#   else:
#     print("That is not a valid number, pick a valid number")


# second try
def roll(num):
    if num.startswith('d'):
        num = randint(1, int(num[1:]))
        print(f"You rolled a {num}.")
    else:
        print("That is not a valid number, pick a valid number.")

# variables that should be tracked
class main_sheet():
  def __init__(self, alignment, age, ):
    self.alignment = input("What is your character's alignment")
    self.age = input("What is your character's age?")
  
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

# Code that needs to be fixed
# # Sample character
# character = Character("Gandalf", "Human", "Wizard", 10, 8, 14, 12, 18, 16, 20)

# # Show character stats
# character.show_stats()