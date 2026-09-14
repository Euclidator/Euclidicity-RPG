def xp_required(level):
    return level * 100


def check_level_up(player):

    while player["xp"] >= xp_required(player["level"]):

        player["xp"] -= xp_required(player["level"])

        player["level"] += 1

        player["max_hp"] += 20
        player["attack"] += 3
        player["defence"] += 2

        player["hp"] = player["max_hp"]

        print()
        print("=" * 40)
        print("          LEVEL UP!")
        print("=" * 40)

        print(f"You reached Level {player['level']}!")

        print()
        print("+20 Maximum HP")
        print("+3 Attack")
        print("+2 Defence")

        print()
        print("Your HP has been fully restored!")

        print("=" * 40)