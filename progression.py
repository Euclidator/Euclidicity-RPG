REGIONS = [
    {
        "name": "Beginner Village",
        "dungeon": "Beginner Dungeon",
        "enemy": "goblin",
        "boss": "Goblin King",
        "story": 1,
    },
    {
        "name": "Bonewatch Village",
        "dungeon": "Skeleton Crypt",
        "enemy": "skeleton",
        "boss": "Skeleton Lord",
        "story": 2,
    },
    {
        "name": "Ironclad Village",
        "dungeon": "Orc Stronghold",
        "enemy": "orc",
        "boss": "Orc Warlord",
        "story": 3,
    },
    {
        "name": "Emberfall Village",
        "dungeon": "Troll Caverns",
        "enemy": "troll",
        "boss": "Troll Chieftain",
        "story": 4,
    },
    {
        "name": "Skyreach Village",
        "dungeon": "Wyvern's Peak",
        "enemy": "wyvern",
        "boss": "Ancient Wyvern",
        "story": 5,
    },
]

BOSS_INTROS = {
    "Goblin King": "The Goblin King raises his crown and snarls: "
                   "\"Kneel before the ruler of the deep!\"",
    "Skeleton Lord": "The Skeleton Lord's empty eyes blaze blue: "
                     "\"Your life will join my endless legion.\"",
    "Orc Warlord": "The Orc Warlord slams his axe into the stone: "
                   "\"Only the strongest leave my fortress alive!\"",
    "Troll Chieftain": "The Troll Chieftain shakes the cavern with a roar: "
                       "\"The mountain itself fights for me!\"",
    "Ancient Wyvern": "The Ancient Wyvern spreads its wings above the peak: "
                     "\"Mortal, you have climbed into my sky.\"",
}


def ensure_progress(player):
    unlocked = player.get("unlocked_region", 0)
    if not isinstance(unlocked, int):
        unlocked = 0

    player["unlocked_region"] = max(0, min(unlocked, len(REGIONS) - 1))
    current = player.get("current_region", 0)
    if not isinstance(current, int):
        current = 0

    player["current_region"] = max(0, min(current, player["unlocked_region"]))
    return player


def current_region(player):
    ensure_progress(player)
    return REGIONS[player["current_region"]]


def show_boss_intro(boss_name):
    print()
    print("=" * 40)
    print(f"          {boss_name.upper()}")
    print("=" * 40)
    print(BOSS_INTROS.get(
        boss_name,
        f"{boss_name} steps forward to challenge you!"
    ))
    print("The air grows tense as the battle begins...")
