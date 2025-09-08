import json
import os

SAVE_FILE = "savegame.json"

def save_game(data: dict):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Game saved successfully!")

def load_game() -> dict | None:
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as f:
        return json.load(f)
