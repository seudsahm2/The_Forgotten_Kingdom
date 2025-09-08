class Enemy:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_player(self,player):
        pass
    
    def take_damage(self,amount):
        pass
    
    def is_alive(self):
        pass
    
class Wolf(Enemy):
    pass

class Bandit(Enemy):
    pass

class ShadowDragon(Enemy):
    pass