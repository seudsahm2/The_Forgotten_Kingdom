# NPC -> non player character
class NPC:
    def __init__(self,name: str,dialogue: str):
        self.name = name
        self.dialogue = dialogue
        
    def talk(self) -> str:
        return f"{self.name}: {self.dialogue}"
    
    def give_item(self, player,item):
        pass