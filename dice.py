import math
import random
from random import randint
from character import *
from classes import *
from races import *
from dictionaries import *


# These will be the dice the character will use. 
def roll(num):
    if num.startswith('d'):
        num = randint(1, int(num[1:]))
        print(f"You rolled a {num}.")
    else:
        print("That is not a valid number, pick a valid number.")
