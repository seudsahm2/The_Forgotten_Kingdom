# NPC -> non player character
from .player import Player
from .item import Item
class NPC:
    def __init__(self,name: str,dialogue: str):
        self.name = name
        self.dialogue = dialogue
        
    def talk(self) -> str:
        return f"{self.name}: {self.dialogue}"
    
    def give_item(self, player: Player,item: Item):
        player.add_item(item)
        print(f"{self.name} givs {player.name} a {item.name}")