from ..core.enemy import ShadowDragon

class DragonLair:
    def enter(self, player):
        print("\n🐉 You step into the Dragon’s Lair...")
        dragon = ShadowDragon()
        return ("battle", dragon)
