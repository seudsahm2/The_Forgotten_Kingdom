
from .npc import NPC
from .item import Item
from .player import Player
from .enemy import Enemy

class Game:
    def __init__(self):
        self.player: Player | None = None
        self.npc: NPC | None = None
        self.started: bool = False
        
    def start(self) -> None:
        if self.started:
            return
        
        print("--The Forgotten Kingdom--")
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
        
        print(f"\nyour current status -- {self.player.status()}")
        
        self.started = True
        
        input("\n[Press ENter to begin your journy...]")
    
    def village(self):
        print("\n -- Village --")
        print(self.elder.talk())
        
        potion = Item(name="Small Potion", effect="heal", value=20)
        self.elder.give_item(self.player,potion)
        
        print(f"Inveentory: {[item.name for item in self.player.inventory]}")
    
    def forest(self):
        pass
    
    def dragon_lair(self):
        pass
    
    def battle(self,player:Player,enemy:Enemy):
        print(f"\n-- Battle starts: {player.name} vs {enemy.name} -- \n")
        while player.is_alive() and enemy.is_alive():
            player.attack_enemy(enemy)
            if not enemy.is_alive():
                print(f"{enemy.name} is defeated\n")
                break
            
            enemy.attack_player(player)
            if not player.is_alive():
                print(f"{player.name} has fallen...")
                break
    
    def game_over(self):
        pass
    
    def victory(self):
        pass