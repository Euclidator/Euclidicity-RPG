import random


def create_beginner_sword():
    return {
        "name": "Beginner Sword",
        "attack_bonus": random.randint(3, 7),
        "price": 50
    }


def create_beginner_armour():
    return {
        "name": "Beginner Armour",
        "defence_bonus": random.randint(3, 6),
        "price": 50
    }


def create_beginner_helmet():
    return {
        "name": "Beginner Helmet",
        "defence_bonus": random.randint(1, 4),
        "price": 30
    }


EQUIPMENT_TIERS = [
    {
        "weapon": ("Beginner Sword", 3, 7, 50),
        "armour": ("Beginner Armour", 3, 6, 50),
        "helmet": ("Beginner Helmet", 1, 4, 30),
    },
    {
        "weapon": ("Boneblade", 7, 11, 100),
        "armour": ("Boneguard Armour", 6, 10, 100),
        "helmet": ("Boneguard Helm", 3, 6, 70),
    },
    {
        "weapon": ("Orcish Cleaver", 11, 16, 160),
        "armour": ("Ironclad Armour", 10, 15, 160),
        "helmet": ("Ironclad Helm", 5, 9, 110),
    },
    {
        "weapon": ("Trollbreaker", 16, 22, 240),
        "armour": ("Trollhide Armour", 15, 21, 240),
        "helmet": ("Trollhide Helm", 8, 13, 170),
    },
    {
        "weapon": ("Wyvernfang", 22, 30, 350),
        "armour": ("Dragonscale Armour", 21, 29, 350),
        "helmet": ("Dragonscale Helm", 12, 18, 250),
    },
]


def create_tier_item(region, slot):
    name, minimum, maximum, price = EQUIPMENT_TIERS[region][slot]
    bonus_key = "attack_bonus" if slot == "weapon" else "defence_bonus"
    return {
        "name": name,
        bonus_key: random.randint(minimum, maximum),
        "price": price,
    }