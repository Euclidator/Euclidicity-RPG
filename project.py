from player import create_player
from village import village
from save_load import load_game
from story import start_story


def display_title():
    """Display the game's main menu heading."""
    print("=" * 40)
    print("          EUCLIDICITY RPG")
    print("=" * 40)


def get_menu_choice():
    """Read and return a valid main-menu choice."""
    print()
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")
    return input("> ").strip()


def new_game():

    print()
    print("=" * 40)
    print("          CREATE YOUR HERO")
    print("=" * 40)

    name = input("Enter your hero's name: ").strip()

    while not name:
        print("Your hero needs a name!")
        name = input("Enter your hero's name: ").strip()

    player = create_player(name)
    start_story(player)
    return player


def main():

    display_title()

    while True:

        choice = get_menu_choice()

        if choice == "1":

            player = new_game()

            village(player)

        elif choice == "2":

            player = load_game()

            if player is not None:
                village(player)

        elif choice == "3":

            print()
            print("Thank you for playing Euclidicity RPG!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()