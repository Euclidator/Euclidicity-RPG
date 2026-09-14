def create_player(name):
    return {
        "name": name,
        "level": 1,
        "hp": 100,
        "max_hp": 100,
        "attack": 10,
        "defence": 5,
        "xp": 0,
        "gold": 100,
        "weapon": None,
        "armour": None,
        "helmet": None,
        "story_progress": 0,
        "unlocked_region": 0,
        "current_region": 0
    }


def rename_player(player, new_name):
    player["name"] = new_name


def get_attack(player):
    attack = player["attack"]

    if player["weapon"] is not None:
        attack += player["weapon"]["attack_bonus"]

    return attack


def get_defence(player):
    defence = player["defence"]

    if player["armour"] is not None:
        defence += player["armour"]["defence_bonus"]

    if player["helmet"] is not None:
        defence += player["helmet"]["defence_bonus"]

    return defence


def equip_item(player, slot, item):
    """Equip one item in a slot, replacing the previous item."""
    if slot not in ("weapon", "armour", "helmet"):
        raise ValueError(f"Invalid equipment slot: {slot}")

    previous_item = player.get(slot)
    player[slot] = item
    return previous_item


def heal_player(player):
    player["hp"] = player["max_hp"]


def take_damage(player, damage):
    player["hp"] -= damage

    if player["hp"] < 0:
        player["hp"] = 0


def add_gold(player, amount):
    player["gold"] += amount


def add_xp(player, amount):
    player["xp"] += amount


def is_alive(player):
    return player["hp"] > 0


def display_defeat_message(player):
    print()
    print("=" * 40)
    print("             DEFEATED")
    print("=" * 40)
    print(f"{player['name']} has fallen in battle.")
    print("Return to the village, rest, and try again!")
    print("=" * 40)


def display_player(player):
    print()
    print("=" * 40)
    print("             CHARACTER")
    print("=" * 40)

    print(f"Name:     {player['name']}")
    print(f"Level:    {player['level']}")
    print(f"XP:       {player['xp']}")
    print(f"HP:       {player['hp']}/{player['max_hp']}")
    print(f"Attack:   {get_attack(player)}")
    print(f"Defence:  {get_defence(player)}")
    print(f"Gold:     {player['gold']}")

    print()
    print("Equipment")
    print("-" * 40)

    if player["weapon"]:
        print(
            f"Weapon: {player['weapon']['name']} "
            f"(+{player['weapon']['attack_bonus']} Attack)"
        )
    else:
        print("Weapon: None")

    if player["armour"]:
        print(
            f"Armour: {player['armour']['name']} "
            f"(+{player['armour']['defence_bonus']} Defence)"
        )
    else:
        print("Armour: None")

    if player["helmet"]:
        print(
            f"Helmet: {player['helmet']['name']} "
            f"(+{player['helmet']['defence_bonus']} Defence)"
        )
    else:
        print("Helmet: None")

    print("=" * 40)
