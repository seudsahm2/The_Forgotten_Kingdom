from ..core.npc import NPC
from ..core.item import Item

class Village:
    def __init__(self):
        self.elder = NPC(
            "Village Elder",
            dialogue=[
                "The north grows darker each night.",
                "Seek the dragon, but beware the forest wolves."
            ],
            trade_items=[Item("Potion", "heal", 20)]
        )

    def enter(self, player):
        print("\n🏘️ You arrive in the Village.")
        self.elder.talk()

        while True:
            print("\nActions:")
            print("1. Talk to Elder")
            print("2. Trade with Elder")
            print("3. Travel to the Forest")
            print("4. Rest (restore some HP)")
            print("5. Save Game")
            print("6. Load Game")
            print("7. Quit Game")

            choice = input("Choose an action: ").strip()

            if choice == "1":
                self.elder.talk()
            elif choice == "2":
                self.elder.trade(player)
            elif choice == "3":
                return "forest"
            elif choice == "4":
                player.heal(10)
                print(f"{player.name} rests and recovers some strength.")
            elif choice == "5":
                from ..utils import save_game
                data = {
                    "player": player.to_dict(),
                    "current_scene": "village"
                }
                save_game(data)
            elif choice == "6":
                from ..utils import load_game
                data = load_game()
                if data:
                    from ..core.player import Player
                    from ..core.item import Item
                    item_lookup = {
                        "Potion": Item("Potion", "heal", 20),
                        "Rusty Sword": Item("Rusty Sword", "attack_boost", 5),
                    }
                    player = Player.from_dict(data["player"], item_lookup)
                    print("✅ Game loaded successfully!")
                else:
                    print("⚠️ No save file found.")
            elif choice == "7":
                return "end"
            else:
                print("Invalid choice.")
