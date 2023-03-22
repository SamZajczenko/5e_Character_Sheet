import math
import random
from tabulate import tabulate
from random import randint
from dice import *
from classes import *
from races import *
from dictionaries import *

scores = [[strength], [dexterity], [constitution], [intelligence], [wisdom], [charisma]]
table_prof_bonus = [[1-4, 2],[5-8, 3],[9-12, 4],[13-16, 5],[17-20, 6]]

# variables that should be tracked
class Main_sheet():
  def __init__(self, alignment, age, prof_bonus,):
    self.alignment = alignment
    self.age = age
    self.prof_bonus = 
  
import tabulate 
  
def race():
  print(tabulate(races, racesfmt = 'fancy_grid'))
  print(input("What is your character race? Choose from the values above. "))

def char_class():
  print(tabulate(classes, classesfmt = 'fancy_grid'))
  print(input("What class is your character? Choose from the list above. "))
  
def character_start():
  name = print(input("What is your character's name? \n")).lower()
  race = race()
  char_class = char_class()
  level = print(input("What level is your character? \n")).lower()
  multi_class = print(input("Would you like to multiclass? (y/n) \n")).lower()
  if multi_class == "yes":
     amount_class = print("How many classes do you want to have? ")
     
  priority = print(input("Do you want to prioritze any modifiers, or follow the book? "))
  if priority.contains(book):
    
  # strength = print(input(""))
  # dexterity = print(input(""))
  # constitution = print(input(""))
  # intelligence = print(input(""))
  # wisdom = print(input(""))
  # charisma = print(input(""))

class Character:
  def __init__(self, name, race, char_class, level, strength, dexterity, constitution, intelligence, wisdom, charisma):
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