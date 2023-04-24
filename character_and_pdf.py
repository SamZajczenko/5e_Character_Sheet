from character import *
from pdf import *

# Everthing passes through character.py then passes through to character_and_pdf.py for character creation
# Running Character Code
name = print(input("What is your character's name? \n"))
races()
race = print(input("What is your character race? Choose from the values above. \n")).lower()
char_classes()
char_class = print(input("What class is your character? Choose from the list above. \n")).lower()
level = print(input("What is your character's level? Choose from 1-20. \n")).lower()


wisdom = passive_wis()
Character(name, race, char_class, level, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)

# If I have extra time. 
# Increase or Feats if correct level.
# Background
# Multi Classing  
# Artificer

# ##################################################################################
# Everything passes through pdf.py then passes into character_and_pdf.py for the sheet creation. 
# Running PDF Creation Code
