class Player:
    def __init__(self,name="Aria",health=100,attack=5):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.inventory = []
        
    def atack_enemy(self, enemy):
        pass
    
    def take_damage(self,amount):
        pass
    
    def heal(self,maount):
        pass
    
    def is_alive(self):
        pass
    
    def add_item(self,item):
        pass
    
    def use_item(self, item_name):
        pass