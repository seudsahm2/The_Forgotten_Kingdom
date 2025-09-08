# boss.py
from .enemy import Enemy
from .item import Item
import random

class ShadowDragon(Enemy):
    def __init__(self):
        # Dragon has huge health and attack
        legendary_sword = Item("Dragon Slayer", "attack_boost", 10)
        super().__init__(name="Shadow Dragon", health=100, attack=15, loot=[legendary_sword])
        self.turn_counter = 0  # track turns for special attack

    def attack_player(self, player):
        """Dragon alternates between normal attack and fire breath."""
        self.turn_counter += 1

        if self.turn_counter % 3 == 0:  # every 3rd turn → fire breath
            damage = self.attack * 2
            print(f"{self.name} breathes FIRE! {player.name} takes {damage} damage!")
            player.take_damage(damage)
        else:
            # normal attack
            super().attack_player(player)

    def intro(self):
        print("\n🔥 The ground shakes... The SHADOW DRAGON emerges from the darkness!")
        print("Its eyes glow crimson as it roars, ready to burn everything to ashes!")
