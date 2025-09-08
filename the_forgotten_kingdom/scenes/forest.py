import random
from ..core.enemy import Wolf, Bandit

class Forest:
    def enter(self, player):
        print("\n🌲 You enter the dark Forest...")
        encounter = random.choice([Wolf(), Bandit(), None])

        if encounter:
            print(f"A wild {encounter.name} appears!")
            return ("battle", encounter)
        else:
            print("The forest is quiet... too quiet.")
            return "dragon_lair"
