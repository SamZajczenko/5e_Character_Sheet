import math
import random
from tabulate import tabulate
from random import randint
from character import *
from dice import *
from races import *
from dictionaries import *

classes = [[barbarian], [bard], [cleric], [druid], [fighter], [monk], [paladin], [ranger], [rogue], [sorcerer], [warlock], [wizard]]

# Dungeons and Dragons classes code
class Character_classes:
  def __init__(self, hit_die, ):
    self.hit_die = 