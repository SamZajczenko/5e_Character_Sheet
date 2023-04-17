import math
import random
from tabulate import tabulate
from random import randint



classes = [[barbarian], [bard], [cleric], [druid], [fighter], [monk], [paladin], [ranger], [rogue], [sorcerer], [warlock], [wizard]]

def char_class():
  print(tabulate(classes, classesfmt = 'fancy_grid'))
  print(input("What class is your character? Choose from the list above. "))

# Dungeons and Dragons classes code
classes