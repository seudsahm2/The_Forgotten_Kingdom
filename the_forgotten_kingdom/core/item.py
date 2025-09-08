

class Item:
    def __init__(self,name: str,effect: str,value: int):
        self.name = name
        self.effect = effect
        self.value = value
        
    def use(self,target):
        if self.effect == "heal":
            target.heal(self.value)
            print(f"{target.name} uses {self.name} and restores {self.value} HP")
        elif self.effect == "attack_boost":
            target.attack += self.value
            print(f"{target.name} uses {self.name} andd gains +{self.value} ATK")
        else:
            print(f"{self.name} has no effect")
            