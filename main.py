from the_forgotten_kingdom.core.game import Game

def main():
    game = Game()
    print("--The Forgotten Kingdom--")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        game.start()
        game.play()
    elif choice == "2":
        if game.load():
            game.play()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
