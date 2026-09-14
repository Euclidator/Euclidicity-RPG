from merchant import merchant
from dungeon import dungeon
from player import display_player, heal_player
from progression import REGIONS, ensure_progress
from save_load import save_game
from story import story_menu


def travel(player):
    ensure_progress(player)
    print()
    print("=" * 40)
    print("             TRAVEL")
    print("=" * 40)

    for index in range(player["unlocked_region"] + 1):
        marker = " (current)" if index == player["current_region"] else ""
        print(f"{index + 1}. {REGIONS[index]['name']}{marker}")
    print(f"{player['unlocked_region'] + 2}. Cancel")

    choice = input("> ").strip()
    if not choice.isdigit():
        print("Invalid choice.")
        return

    selected = int(choice) - 1
    if 0 <= selected <= player["unlocked_region"]:
        player["current_region"] = selected
        print(f"You travel to {REGIONS[selected]['name']}.")
    elif selected != player["unlocked_region"] + 1:
        print("Invalid choice.")


def village(player):
    ensure_progress(player)

    while True:
        region = REGIONS[player["current_region"]]
        print()
        print("=" * 40)
        print(f"          {region['name'].upper()}")
        print("=" * 40)
        print(f"Hero: {player['name']}")
        print(f"HP: {player['hp']}/{player['max_hp']}")
        print(f"Gold: {player['gold']}")
        print(f"Level: {player['level']}")
        print()
        print("1. Visit Merchant")
        print(f"2. Enter {region['dungeon']}")
        print("3. Character")
        print("4. Rest")
        print("5. Rename Hero")
        print("6. Save Game")
        print("7. Story")
        print("8. Travel")
        print("9. Leave Game")

        choice = input("> ").strip()
        if choice == "1":
            merchant(player)
        elif choice == "2":
            dungeon(player)
        elif choice == "3":
            display_player(player)
        elif choice == "4":
            heal_player(player)
            print()
            print("You rested at the village.")
            print("Your HP has been fully restored.")
        elif choice == "5":
            new_name = input("Enter your hero's new name: ").strip()
            if new_name:
                player["name"] = new_name
                print(f"Your hero is now called {new_name}!")
            else:
                print("Name cannot be empty.")
        elif choice == "6":
            save_game(player)
        elif choice == "7":
            story_menu(player)
        elif choice == "8":
            travel(player)
        elif choice == "9":
            print()
            print("Leaving Euclidicity RPG...")
            return
        else:
            print("Invalid choice.")
