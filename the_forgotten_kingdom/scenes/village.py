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
            print("5. Quit Game")

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
                return "end"
            else:
                print("Invalid choice.")
