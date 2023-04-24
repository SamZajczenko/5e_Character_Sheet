
class Race:
    def __init__(self, speed, score, darkvision, abilities, language):
        self.speed = speed
        self.score = score
        self.darkvision = darkvision
        self.abilities = abilities
        self.language = language
        
    
    # # This is to choose a what abilty scores you would like to increase.
    # # def race_mod():
    # #     num = [0,1,2,3,4,5,6,7,8,9]
    # #     for i in range(len(num)):
    # #         if races[i] == race:
    # #             races[i] += 1
    # #             print("Complete.")

    # # def score_increase():
    # #     print(tabulate(scores, classesfmt = 'fancy_grid'))
    # #     amount = 
    # #     which = print(input(f'What scores would you like to increase, you may choose {amount}. Choose from the list above. '))
    # #     if which.contains(strength):
            
    # #     elif which.contains(dexterity):

    # #     elif which.contains(constitution):
            
    # #     elif which.contains(intelligence):
            
    # #     elif which.contains(wisdom):
            
    # #     elif which.contains(charisma):
            
    # #     else:
    # #         return None

    # # The races of dnd. I am going to have a main function and then subdivisions.
    # races = [["dwarf"],["elf"],["halfling"],["human"],["dragonborn"],["gnome"],["half_elf"],["half_orc"],["tiefling"]]

class Dwarf(Race):
    def __init__(self, hill=False, mountain=False):
        abilities = ["darkvision", "dwarven resilience", "stonecunning"]
        if hill:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven toughness")
        elif mountain:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
            self.abilities.append("dwarven armor training")
        else:
            super().__init__(speed=25, score=[2,0,2,0,0,2], darkvision=True, abilities=abilities, language="Common, Dwarvish")
    
class Elf(Race):
    def __init__(self, wood=False, drow=False, high=False):
        abilities = ["darkvision", "keen sense", "fey ancestry", "trance"]
        if wood:
            super().__init__(speed=35, score=[0,2,0,0,1,0], darkvision=True, abilities=abilities, language="Common, Elvish")
            self.abilities.append("mask of the wild","elf weapon training")
        elif drow:
            super().__init__(speed=30, score=[0,2,0,0,0,1], darkvision=True, abilities=abilities, language="Common, Elvish")
            self.abilities.append("elf weapon training", "cantrip")
        elif high:
            super().__init__(speed=30, score=[0,2,0,1,0,0], darkvision=False, abilities=abilities, language="Common, Elvish")
            self.abilities.append("superior darkvision", "sunlight sensitivity", "drow magic", "drow weapon casting")
        else:
            super().__init__(speed=30, score=[0,2,0,0,0,0], darkvision=False, abilities=abilities, language="Common, Elvish")

class Halfling(Race):
    def __init__(self, lightfoot=False, stout=False):
        abilities = ["lucky", "halfling nimbleness", "brave"]
        if lightfoot:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")
            self.abilities.append("naturally stealthy")
        elif stout:
            super().__init__(speed=25, score=[0, 2, 1, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")
            self.abilities.append("stout resilience")
        else:
            super().__init__(speed=25, score=[0, 2, 0, 0, 0, 0], darkvision=False, abilities=abilities, languages="Common, Halfling")

class Human(Race):
  def __init__(self, variant=False):
      abilities = [none]
      if variant == True:
        super().__init__(speed=30, score=[1,1,1,1,1,1], darkvision=False, abilities=abilities, language="Common, ")
      else:
          super().__init__(speed=30, score=[], darkvision=False, abilities=None, languages="Common, ")

class Dragonborn(Race):
  def __init__(self, speed, score, darkvision, abilities, language):
      super().__init__(speed=30, score=[], darkvision=True, abilities=abilities, language="Common, ")
  
class Gnome(Race):
  def __init__(self, speed, score, darkvision, abilities, language):
      super().__init__(speed=30, score=[], darkvision=True, abilities=abilities, language="Common, and Gnomish")

class Half_elf(Race):
    def __init__(self, score):
        abilities = ["darkvision", "fey ancestry", "skill versatility"]
        super().__init__(speed=30, score=score, darkvision=True, abilities=abilities, languages="Common, Elvish")

class Half_orc(Race):
    def __init__(self, score):
        abilities = ["darkvision", "menacing", "relentless endurance", "savage attacks"]
        super().__init__(speed=30, score=score, darkvision=True, abilities=abilities, languages="Common, Orcish")

class Tiefling(Race):
    def __init__(self, speed=30, score=[0, 0, 0, 1, 0, 2], darkvision=True, abilities=["hellish resistance", "infernal legacy"], language="Common, Infernal"):
        super().__init__(speed, score, darkvision, abilities, language)
