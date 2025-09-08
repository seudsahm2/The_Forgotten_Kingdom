
from .npc import NPC
from .item import Item
from .player import Player
from .enemy import Enemy
from .boss import ShadowDragon

from ..scenes.village import Village
from ..scenes.forest import Forest
from ..scenes.dragon_lair import DragonLair

from ..utils import load_game
from ..utils import save_game

class Game:
    def __init__(self):
        self.player: Player | None = None
        self.npc: NPC | None = None
        self.started: bool = False
        self.scenes = {
            "village": Village(),
            "forest": Forest(),
            "dragon_lair": DragonLair()
        }
        self.current_scene = "village"
        
    def play(self):
        while self.current_scene != "end":
            scene = self.scenes.get(self.current_scene)

            if not scene:
                print("Unknown scene. Game over.")
                break

            result = scene.enter(self.player)

            if isinstance(result, tuple) and result[0] == "battle":
                enemy = result[1]
                self.battle(self.player, enemy)
                if not self.player.is_alive():
                    self.game_over()
                    break
                self.current_scene = "forest" if enemy.name != "Shadow Dragon" else "end"
            else:
                self.current_scene = result
        
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
            name="Village Elder",
            dialogue=[
                "Darkness gathers in the north.",
                "Cross the forest and seek the ruined castle.",
                "There, a Shadow Dragon guards the truth of Elaria."
            ]
        )

        
        print(self.elder.dialogue)
        
        print(f"\nyour current status -- {self.player.status()}")
        
        self.started = True
        
        input("\n[Press ENter to begin your journy...]")
    

        pass
    
    def meet_npc(self, player):
        healer = NPC(
            "Wise Healer",
            dialogue=[
                "The Shadow Dragon grows stronger every night...",
                "Take care of your wounds, brave warrior.",
                "Potions are your best friend in dark times."
            ],
            trade_items=[Item("Potion", "heal", 30), Item("Elixir", "heal", 50)]
        )

        healer.talk()
        healer.trade(player)
    
    def battle(self,player:Player,enemy:Enemy):
        
        print(f"\nA wild {enemy.name} appears!")
        
        while player.is_alive() and enemy.is_alive():
            print("\nYour turn")
            print("1. Atatck")
            print("2.Use Item")
            choice = input("choose acion:").strip()
            
            if choice == "1":
                player.attack_enemy(enemy)
            elif choice == "2":
                if not player.inventory:
                    print("⚠️ You have no items!")
                    continue
                print("Inventory:", [item.name for item in player.inventory])
                item_name = input("Enter item name to use: ").strip()
                if not player.use_item(item_name):
                    continue

            else:
                print("Invalid choice try again")
                continue
            
            if enemy.is_alive():
                enemy.attack_player(player)
            
            
        if player.is_alive():
             print(f"You defeated {enemy.name}!")
             loot = enemy.drop_loot()
             if loot:
                 player.add_item(loot)
        else:
            self.game_over()
            
    def final_battle(self, player):
        dragon = ShadowDragon()
        dragon.intro()
        self.battle(player, dragon)

        if player.is_alive():
            print("\n🎉 Congratulations! You defeated the Shadow Dragon and restored peace to the kingdom!")
        else:
            self.game_over()
    
    def game_over(self):
        pass
    
    def victory(self):
        pass
    
    def save(self):
        data = {
            "player": self.player.to_dict(),
            "current_scene": self.current_scene
        }
        save_game(data)

    def load(self):
        data = load_game()
        if not data:
            print("⚠️ No save file found.")
            return False

        # Rebuild player with item lookup
        item_lookup = {
            "Potion": Item("Potion", "heal", 20),
            "Rusty Sword": Item("Rusty Sword", "attack_boost", 5)
        }
        self.player = Player.from_dict(data["player"], item_lookup)
        self.current_scene = data["current_scene"]
        print(f"✅ Game loaded. Welcome back, {self.player.name}!")
        return True
    