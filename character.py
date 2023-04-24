from probabilities import *
from classes import *

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
    if char_class == classes[0]:
      Barbarian.scores(player_scores)
    elif char_class == classes[1]:
      Bard.scores(player_scores)
    elif char_class == classes[2]:
      Cleric.scores(player_scores)
    elif char_class == classes[3]:
      Druid.scores(player_scores)
    elif char_class == classes[4]:
      Fighter.scores(player_scores)
    elif char_class == classes[5]:
      Monk.scores(player_scores)
    elif char_class == classes[6]:
      Paladin.scores(player_scores)
    elif char_class == classes[7]:
      Ranger.scores(player_scores)
    elif char_class == classes[8]:
      Rogue.scores(player_scores)
    elif char_class == classes[9]:
      Sorcerer.scores(player_scores)
    elif char_class == classes[10]:
      Warlock.scores(player_scores)
    elif char_class == classes[11]:
      Wizard.scores(player_scores)
    else:
      None