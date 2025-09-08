from random import choice

class Enemy:
    def __init__(self,name: str,health: int,attack: int, loot: list = None):
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        self.loot = loot or []
    
      
    def attack_player(self,player:"Player"):
        from .player import Player  
        print(f"{self.name} attacks {player.name} for {self.attack} damage")
        player.take_damage(self.attack)
    
    def take_damage(self,amount:int):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} taks {amount} damage (HP left: {self.health}XP)")
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def drop_loot(self):
        if not self.loot:
            return None
        dropped = choice(self.loot)
        print(f"{self.name} dropped {dropped.name}")
        return dropped
        
    
class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf",health=30,attack=5)

class Bandit(Enemy):
    def __init__(self):
        from .item import Item
        sword = Item("Rusty Sword","attck_boost",3)
        potion = Item("Potion","heal",20)
        super().__init__(name="Bandit",health=50,attack=10,loot=[sword,potion])

class ShadowDragon(Enemy):
    def __init__(self):
        super().__init__(name="Shadow Dragon",health=150,attack=20)