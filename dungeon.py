from enemies import create_region_enemy, create_region_boss
from combat import combat
from leveling import check_level_up
from player import add_gold, add_xp
from progression import REGIONS, ensure_progress, show_boss_intro
from story import advance_story


def give_reward(player, enemy):
    gold = enemy["gold"]
    xp = enemy["xp"]
    add_gold(player, gold)
    add_xp(player, xp)

    print()
    print("=" * 40)
    print("             REWARDS")
    print("=" * 40)
    print(f"Gold: +{gold}")
    print(f"XP:   +{xp}")
    check_level_up(player)


def dungeon_stage(player, stage, region_index=None):
    if region_index is None:
        region_index = player.get("current_region", 0)

    print()
    print("=" * 40)
    print(f"          DUNGEON STAGE {stage}")
    print("=" * 40)

    for _ in range(stage):
        enemy = create_region_enemy(region_index)
        print()
        print(f"A {enemy['name']} appears!")
        if not combat(player, enemy):
            return False
        give_reward(player, enemy)
    return True


def dungeon(player):
    ensure_progress(player)
    region_index = player["current_region"]
    region = REGIONS[region_index]

    print()
    print("=" * 40)
    print(f"        {region['dungeon'].upper()}")
    print("=" * 40)

    for stage in range(1, 5):
        if not dungeon_stage(player, stage, region_index):
            return False
        print()
        print(f"Stage {stage} cleared!")
        if stage < 4:
            choice = input("Continue to the next stage? (Y/N): ").strip().lower()
            if choice != "y":
                return True

    print()
    print("=" * 40)
    print("          FINAL STAGE")
    print("=" * 40)
    advance_story(player, region["story"])
    print()
    print(f"The {region['boss']} appears!")
    print("Prepare yourself!")

    boss = create_region_boss(region_index)
    show_boss_intro(boss["name"])
    if not combat(player, boss):
        return False

    give_reward(player, boss)
    print()
    print("=" * 40)
    print("       DUNGEON CLEARED!")
    print("=" * 40)
    print(f"You defeated the {region['boss']}!")

    if region_index < len(REGIONS) - 1:
        player["unlocked_region"] = max(
            player["unlocked_region"], region_index + 1
        )
        print(f"{REGIONS[region_index + 1]['name']} is now accessible!")
        advance_story(player, region["story"] + 1)
    else:
        advance_story(player, 6)
        print("The Crystal Compass has been restored!")
    return True
