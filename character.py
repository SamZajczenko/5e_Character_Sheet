import math
import random
from tabulate import tabulate
from random import randint

scores = [[strength], [dexterity], [constitution], [intelligence], [wisdom], [charisma]]
table_prof_bonus = [[[0][4], 2],[5-8, 3],[9-12, 4],[13-16, 5],[17-20, 6]]
  
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
     
  priority = print(input("Do you want to prioritize any modifiers, or follow the book's recommended rules? "))
  if priority.contains("book"):
    pass
  elif priority.contains("prioritize"):
    strength = print(input(""))
  # dexterity = print(input(""))
  # constitution = print(input(""))
  # intelligence = print(input(""))
  # wisdom = print(input(""))
  # charisma = print(input(""))
  else:
    None

class Character:
  def __init__(self,name,race,char_class,level,strength,dexterity,constitution,intelligence,wisdom,charisma,skill_prof,armor_class,hit_points,weapons,equipment,gen_prof,personality_traits,ideals,bonds,flaws, features_traits):
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
      self.skill_prof = skill_prof
      self.armor_class = armor_class
      self.hit_points = hit_points
      self.weapons = weapons
      self.equipment = equipment
      self.gen_prof = gen_prof
      self.personality_traits = personality_traits 
      self.ideals = ideals
      self.bonds = bonds
      self.flaws = flaws
      self.features_traits = features_traits