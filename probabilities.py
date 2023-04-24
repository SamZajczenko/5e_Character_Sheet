import math
import random
from random import randint

# These will be the dice the character will use. 
# num = (int(input("What sided dice? ")))
def roll(num):
    if num in (6, 8, 10, 12, 20):
        result = random.randint(1, num)
        print(f"You rolled a {result}.")
    else:
        print("That is not a valid number, pick a valid number.")
        
num_computer = None
def roll_computer(num_computer):
    if num_computer in (6, 8, 10, 12, 20):
        result = random.randint(1, num_computer)
        return result
    else:
        return None

# # Random values and lists that are helful. 
# languages_main = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic"]

# # Probability of list being chosen
# languages_probabilities = (random.choices(languages_main, weights=(20, 10, 10, 5, 10, 10, 10, 5, 5, 5, 10), k=other))
