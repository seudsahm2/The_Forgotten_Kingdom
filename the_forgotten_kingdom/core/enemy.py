
class Enemy:
    def __init__(self,name: str,health: int,attack: int):
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        
    def attack_player(self,player:"Player"):
        from .player import Player
        print(f"{self.name} attacks {player.name} for {self.attack} damage")
        player.take_damage(self.attack)
    
    def take_damage(self,amount:int):
        self.health -= amount
        print(f"{self.name} taks {amount} damage (HP left: {self.health}XP)")
    
    def is_alive(self):
        pass
    
class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf",health=30,attack=5)

class Bandit(Enemy):
    def __init__(self):
        super().__init__(name="Bandit",health=50,attack=10)

class ShadowDragon(Enemy):
    def __init__(self):
        super().__init__(name="Shadow Dragon",health=150,attack=20)