from .player import Player
from .enemy import Wolf,Bandit,ShadowDragon
from .item import Item
from .npc import NPC

class Game:
    def __init__(self):
        self.player = None
        self.npc = None
        self.enemies = []
        
    def start(self):
        pass
    
    def village(self):
        pass
    
    def forest(self):
        pass
    
    def dragon_lair(self):
        pass
    
    def battle(self,player,enemy):
        pass
    
    def game_over(self):
        pass
    
    def victory(self):
        pass