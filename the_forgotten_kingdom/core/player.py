

class Player:
    def __init__(self,name: str ="Aria",health: int =100,attack: int =5):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.inventory = []
        
    def status(self) -> str:
        return f"{self.name}: HP {self.health}/{self.max_health}, ATK {self.attack}"
    
    from .enemy import Enemy    
    def attack_enemy(self, enemy:Enemy):
        
        print(f"{self.name} aattacks {enemy.name} for {self.attack} damage")
        enemy.take_damage(self.attack)
    
    def take_damage(self,amount:int):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! (HP left: {self.health})")
        if self.health <0:
            self.health = 0
    
    def heal(self,amount:int):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals {amount} HP! (Current HP: {self.health})")
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    from .item import Item
    def add_item(self,item: Item):
        self.inventory.append(item)
        print(f"{self.name} picks up {item.name}")
    
    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                return True
        print(f"{self.name} does not have a {item_name}")
        return False