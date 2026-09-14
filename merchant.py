from equipment import EQUIPMENT_TIERS, create_tier_item
from player import equip_item
from progression import ensure_progress, current_region


def merchant(player):
    ensure_progress(player)
    region = player["current_region"]
    tier = current_region(player)["name"]

    while True:

        print()
        print("=" * 40)
        print("             MERCHANT")
        print("=" * 40)

        print(f"Gold: {player['gold']}")

        print()
        print(f"Equipment available in {tier}:")
        prices = EQUIPMENT_TIERS[region]
        print(f"1. {prices['weapon'][0]}     {prices['weapon'][3]} Gold")
        print(f"2. {prices['armour'][0]}    {prices['armour'][3]} Gold")
        print(f"3. {prices['helmet'][0]}     {prices['helmet'][3]} Gold")
        print("4. Leave")

        choice = input("> ").strip()

        if choice == "1":

            item = create_tier_item(region, "weapon")
            if player["gold"] < item["price"]:
                print("You don't have enough gold.")
                continue

            player["gold"] -= item["price"]
            previous_item = equip_item(player, "weapon", item)

            print()
            print(f"You purchased a {item['name']}!")
            if previous_item:
                print(f"It replaced your {previous_item['name']}.")
            print(
                f"Attack Bonus: +{item['attack_bonus']}"
            )

        elif choice == "2":

            item = create_tier_item(region, "armour")
            if player["gold"] < item["price"]:
                print("You don't have enough gold.")
                continue

            player["gold"] -= item["price"]
            previous_item = equip_item(player, "armour", item)

            print()
            print(f"You purchased {item['name']}!")
            if previous_item:
                print(f"It replaced your {previous_item['name']}.")
            print(
                f"Defence Bonus: +{item['defence_bonus']}"
            )

        elif choice == "3":

            item = create_tier_item(region, "helmet")
            if player["gold"] < item["price"]:
                print("You don't have enough gold.")
                continue

            player["gold"] -= item["price"]
            previous_item = equip_item(player, "helmet", item)

            print()
            print(f"You purchased a {item['name']}!")
            if previous_item:
                print(f"It replaced your {previous_item['name']}.")
            print(
                f"Defence Bonus: +{item['defence_bonus']}"
            )

        elif choice == "4":
            return

        else:
            print("Invalid choice.")