# npc.py
from .item import Item
from typing import List

class NPC:
    def __init__(self, name: str, dialogue: List[str], trade_items: List[Item] = None):
        self.name = name
        self.dialogue = dialogue  # list of possible dialogue lines
        self.trade_items = trade_items if trade_items else []

    def talk(self):
        """NPC introduces themselves and says their dialogue."""
        print(f"\n👤 {self.name} says:")
        for line in self.dialogue:
            print(f"  - {line}")

    def trade(self, player):
        """Offer trade items to the player."""
        if not self.trade_items:
            print(f"{self.name} has nothing to trade right now.")
            return

        print(f"\n💰 {self.name} offers the following items:")
        for idx, item in enumerate(self.trade_items, start=1):
            print(f"{idx}. {item.name} — {item.effect} (+{item.effect})")

        choice = input("Enter the item number to take (or press Enter to cancel): ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(self.trade_items):
                item = self.trade_items.pop(idx)
                player.add_item(item)
                print(f"{player.name} received {item.name}!")
            else:
                print("Invalid choice.")
