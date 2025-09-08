class Player:
    def __init__(self,name: str ="Aria",health: int =100,attack: int =5):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.inventory = []
        
    def status(self) -> str:
        return f"{self.name}: HP {self.health}/{self.max_health}, ATK {self.attack}"
        
    def atack_enemy(self, enemy):
        pass
    
    def take_damage(self,amount):
        pass
    
    def heal(self,maount):
        pass
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    def add_item(self,item):
        pass
    
    def use_item(self, item_name):
        pass