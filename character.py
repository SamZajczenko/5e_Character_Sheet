import math
import random
from probabilities import *


classes = [[barbarian], [bard], [cleric], [druid], [fighter], [monk], [paladin], [ranger], [rogue], [sorcerer], [warlock], [wizard]]
races = [["dwarf"],["elf"],["halfling"],["human"],["dragonborn"],["gnome"],["half_elf"],["half_orc"],["tiefling"]]
scores = [[strength], [dexterity], [constitution], [intelligence], [wisdom], [charisma]]
# Level then bonus. 
table_prof_bonus = [0-4, 2],[5-8, 3],[9-12, 4],[13-16, 5],[17-20, 6] 

def race():
  print(tabulate(races, racesfmt = 'fancy_grid'))

def char_class():
  print(tabulate(classes, classesfmt = 'fancy_grid'))
  
name = None
char_race = None
class_choice = None
level = None

def character_start(name, char_race, class_choice, level):
  name = print(input("What is your character's name? \n")).lower()
  
  race()
  char_race = print(input("What is your character race? Choose from the values above. "))
  
  char_class()
  class_choice = print(input("What class is your character? Choose from the list above. "))
  
  level = print(input("What is your character's level? Choose from 1-20. ")).lower()
  
  return name, char_race, class_choice, level
  
  # Increase or Feats if correct level.
  # Background
  # Multi Classing  
  # multi_class = print(input("Would you like to multiclass? (y/n) \n")).lower()
  # if multi_class == "yes":
  #    amount_class = print("How many classes do you want to have? ")
  
def scores():
    num_computer = 6
    list = []
    for i in range(4):
        list.append(roll_computer(num_computer))
    list.sort(reverse=True)
    total = sum(list[:3])
    return total
  
def ability_scores(char_class):
  player_scores = []
  for i in range(6):
    player_scores.append(scores())
  player_scores.sort(reverse=True)
  if class_choice == classes[0]:

  elif class_choice == classes[1]:

  elif class_choice == classes[2]:

  elif class_choice == classes[3]:

  elif class_choice == classes[4]:

  elif class_choice == classes[5]:

  elif class_choice == classes[6]:

  elif class_choice == classes[7]:

  elif class_choice == classes[8]:

  elif class_choice == classes[9]:

  elif class_choice == classes[10]:

  elif class_choice == classes[11]:

  else:
    None
    
    

modifiers = [(-5, i) if i == 0 else ((i - 1) // 2 - 5, i) for i in range(31)]

def passive_wis(wisdom, modifiers):
  i = wisdom
  passive_wisdom = 10 + modifiers(i) 
  return passive_wisdom  

class Character:
  def __init__(self,name,race,char_class,level,strength,dexterity,constitution,intelligence,wisdom,charisma,skill_prof,armor_class,hit_points,weapons,equipment,all_prof,personality_traits,ideals,bonds,flaws, features_traits, spells, spell_save_DC, spell_attack_bonus):
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
      self.all_prof = all_prof
      self.personality_traits = personality_traits 
      self.ideals = ideals
      self.bonds = bonds
      self.flaws = flaws
      self.features_traits = features_traits
      self.spells = spells
      self.spell_save_DC = spell_save_DC
      self.spell_attack_bonus = spell_attack_bonus