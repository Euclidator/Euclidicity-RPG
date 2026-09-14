import random

from player import (
    get_attack,
    get_defence,
    take_damage,
    display_defeat_message
)
from enemies import is_alive


def calculate_player_damage(player, enemy):
    attack = get_attack(player)

    minimum_damage = max(1, attack // 2)

    damage = random.randint(
        minimum_damage,
        attack
    )

    damage -= enemy["defence"]

    return max(1, damage)


def calculate_enemy_damage(player, enemy):
    defence = get_defence(player)

    minimum_defence = max(1, defence // 2)

    defence_roll = random.randint(
        minimum_defence,
        defence
    )

    damage = enemy["attack"] - defence_roll

    return max(1, damage)


def player_attack(player, enemy):
    attack_roll = random.randint(1, 20)

    print()
    print(f"{player['name']} attacks!")

    if attack_roll == 1:
        print("You completely missed!")
        return

    damage = calculate_player_damage(player, enemy)

    if attack_roll == 20:
        damage *= 2
        print("⚔ CRITICAL HIT! ⚔")

    enemy["hp"] -= damage

    if enemy["hp"] < 0:
        enemy["hp"] = 0

    print(f"Attack Roll: {attack_roll}")
    print(f"You dealt {damage} damage!")


def enemy_attack(player, enemy):
    print()
    print(f"{enemy['name']} attacks!")

    damage = calculate_enemy_damage(player, enemy)

    take_damage(player, damage)

    print(f"{enemy['name']} dealt {damage} damage!")
    print(f"{player['name']} HP: {player['hp']}/{player['max_hp']}")


def combat(player, enemy):
    print()
    print("=" * 40)
    print(f"        BATTLE: {enemy['name']}")
    print("=" * 40)

    while is_alive(player) and is_alive(enemy):

        print()
        print(f"{player['name']}: {player['hp']}/{player['max_hp']} HP")
        print(f"{enemy['name']}: {enemy['hp']}/{enemy['max_hp']} HP")

        print()
        print("1. Attack")
        print("2. Defend")
        print("3. Run")

        choice = input("> ").strip()

        if choice == "1":

            player_attack(player, enemy)

            if not is_alive(enemy):
                print()
                print(f"You defeated the {enemy['name']}!")
                return True

            enemy_attack(player, enemy)

        elif choice == "2":

            print()
            print("You prepare to defend!")

            defence = get_defence(player)

            defence_roll = random.randint(
                defence,
                defence * 2
            )

            damage = max(
                0,
                enemy["attack"] - defence_roll
            )

            take_damage(player, damage)

            print(f"You blocked most of the attack!")
            print(f"Damage received: {damage}")

        elif choice == "3":

            escape_roll = random.randint(1, 100)

            if escape_roll <= 50:
                print("You successfully escaped!")
                return False

            print("You failed to escape!")

            enemy_attack(player, enemy)

        else:
            print("Invalid choice.")

    if not is_alive(player):
        display_defeat_message(player)
        return False

    return False