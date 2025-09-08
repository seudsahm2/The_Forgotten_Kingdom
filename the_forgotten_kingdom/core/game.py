from .player import Player
from .enemy import Wolf,Bandit,ShadowDragon
from .item import Item
from .npc import NPC

class Game:
    def __init__(self):
        self.player: Player | None = None
        self.npc: NPC | None = None
        self.started: bool = False
        
    def start(self) -> None:
        if self.started:
            return
        
        print("--The Forgotten Kingddom--")
        print("You awaken in a ruined village under a pale morning sun.\n")
        
        name = input("What is your name travelor? (Press Enter for 'Aria'): ").strip()
        if not name:
            name = "Aria"
        
        self.player = Player(name=name)
        
        self.elder = NPC(
            name = "Village Elder",
            dialogue=(
                "Darkness gathers in the north. Cross the forest and seek the ruined castle. "
                "There, a Shadow Dragon guards the truth of Elaria."
            ),
        )
        
        print(self.elder.dialogue)
        
        print("f\nyour current status -- {self.player.status}")
        
        self.started = True
        
        input("\n[Press ENter to begin your journy...]")
    
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