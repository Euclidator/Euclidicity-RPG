import random


def create_goblin():
    hp = random.randint(20, 30)

    return {
        "name": "Goblin",
        "hp": hp,
        "max_hp": hp,
        "attack": random.randint(5, 8),
        "defence": random.randint(2, 4),
        "xp": random.randint(15, 25),
        "gold": random.randint(10, 20)
    }


def create_goblin_king():
    return {
        "name": "Goblin King",
        "hp": 100,
        "max_hp": 100,
        "attack": random.randint(10, 15),
        "defence": random.randint(6, 9),
        "xp": 150,
        "gold": 100,
        "boss": True
    }


def _create_enemy(name, hp_range, attack_range, defence_range, xp_range,
                  gold_range):
    hp = random.randint(*hp_range)
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "attack": random.randint(*attack_range),
        "defence": random.randint(*defence_range),
        "xp": random.randint(*xp_range),
        "gold": random.randint(*gold_range)
    }


def create_skeleton():
    return _create_enemy("Skeleton", (35, 45), (8, 11), (4, 6), (30, 40),
                         (20, 30))


def create_orc():
    return _create_enemy("Orc", (50, 65), (11, 15), (6, 9), (45, 60),
                         (30, 45))


def create_troll():
    return _create_enemy("Troll", (70, 90), (15, 20), (8, 12), (65, 85),
                         (45, 65))


def create_wyvern():
    return _create_enemy("Wyvern", (90, 115), (19, 25), (11, 15), (90, 115),
                         (60, 85))


def create_region_boss(region):
    bosses = {
        0: create_goblin_king,
        1: lambda: _create_enemy("Skeleton Lord", (130, 150), (16, 21),
                                 (9, 12), (180, 210), (120, 150)),
        2: lambda: _create_enemy("Orc Warlord", (170, 195), (20, 26),
                                 (12, 16), (240, 280), (160, 200)),
        3: lambda: _create_enemy("Troll Chieftain", (220, 250), (24, 31),
                                 (15, 20), (320, 370), (220, 270)),
        4: lambda: _create_enemy("Ancient Wyvern", (280, 320), (29, 37),
                                 (18, 24), (450, 520), (300, 375)),
    }
    return bosses[region]()


def create_region_enemy(region):
    enemies = [create_goblin, create_skeleton, create_orc, create_troll,
               create_wyvern]
    return enemies[region]()


def is_alive(enemy):
    return enemy["hp"] > 0


def display_enemy(enemy):
    print()
    print("-" * 40)
    print(f"{enemy['name']}")
    print("-" * 40)
    print(f"HP:       {enemy['hp']}/{enemy['max_hp']}")
    print(f"Attack:   {enemy['attack']}")
    print(f"Defence:  {enemy['defence']}")
    print("-" * 40)