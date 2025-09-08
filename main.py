from the_forgotten_kingdom.core.game import Game
from the_forgotten_kingdom.core.player import Player

game = Game()
player = Player()

print("\n--- Visiting NPC ---")
game.meet_npc(player)

print("\nInventory after meeting NPC:", [item.name for item in player.inventory])
