import pytest
import save_load

from player import (
    create_player,
    rename_player,
    get_attack,
    get_defence,
    heal_player,
    take_damage,
    add_gold,
    add_xp,
    is_alive
)

from equipment import (
    create_beginner_sword,
    create_beginner_armour,
    create_beginner_helmet
)

from enemies import (
    create_goblin,
    create_goblin_king
)

from combat import (
    calculate_player_damage,
    calculate_enemy_damage
)

from leveling import (
    xp_required,
    check_level_up
)

# PLAYER TESTS

def test_create_player():

    player = create_player("TestHero")

    assert player["name"] == "TestHero"
    assert player["level"] == 1
    assert player["hp"] == 100
    assert player["max_hp"] == 100
    assert player["attack"] == 10
    assert player["defence"] == 5
    assert player["xp"] == 0
    assert player["gold"] == 100


def test_rename_player():

    player = create_player("TestHero")

    rename_player(player, "Arthur")

    assert player["name"] == "Arthur"


def test_get_attack_without_weapon():

    player = create_player("TestHero")

    assert get_attack(player) == 10


def test_get_attack_with_weapon():

    player = create_player("TestHero")

    player["weapon"] = {
        "name": "Test Sword",
        "attack_bonus": 6
    }

    assert get_attack(player) == 16


def test_get_defence_without_equipment():

    player = create_player("TestHero")

    assert get_defence(player) == 5


def test_get_defence_with_armour():

    player = create_player("TestHero")

    player["armour"] = {
        "name": "Test Armour",
        "defence_bonus": 5
    }

    assert get_defence(player) == 10


def test_get_defence_with_armour_and_helmet():

    player = create_player("TestHero")

    player["armour"] = {
        "name": "Test Armour",
        "defence_bonus": 5
    }

    player["helmet"] = {
        "name": "Test Helmet",
        "defence_bonus": 2
    }

    assert get_defence(player) == 12


def test_heal_player():

    player = create_player("TestHero")

    player["hp"] = 25

    heal_player(player)

    assert player["hp"] == 100


def test_take_damage():

    player = create_player("TestHero")

    take_damage(player, 30)

    assert player["hp"] == 70


def test_take_damage_cannot_go_below_zero():

    player = create_player("TestHero")

    take_damage(player, 500)

    assert player["hp"] == 0


def test_add_gold():

    player = create_player("TestHero")

    add_gold(player, 50)

    assert player["gold"] == 150


def test_add_xp():

    player = create_player("TestHero")

    add_xp(player, 50)

    assert player["xp"] == 50


def test_player_is_alive():

    player = create_player("TestHero")

    assert is_alive(player)


def test_player_is_dead():

    player = create_player("TestHero")

    player["hp"] = 0

    assert not is_alive(player)

# EQUIPMENT TESTS

def test_beginner_sword():

    sword = create_beginner_sword()

    assert sword["name"] == "Beginner Sword"
    assert 3 <= sword["attack_bonus"] <= 7
    assert sword["price"] == 50


def test_beginner_armour():

    armour = create_beginner_armour()

    assert armour["name"] == "Beginner Armour"
    assert 3 <= armour["defence_bonus"] <= 6
    assert armour["price"] == 50


def test_beginner_helmet():

    helmet = create_beginner_helmet()

    assert helmet["name"] == "Beginner Helmet"
    assert 1 <= helmet["defence_bonus"] <= 4
    assert helmet["price"] == 30

# ENEMY TESTS

def test_create_goblin():

    goblin = create_goblin()

    assert goblin["name"] == "Goblin"
    assert 20 <= goblin["hp"] <= 30
    assert 5 <= goblin["attack"] <= 8
    assert 2 <= goblin["defence"] <= 4
    assert goblin["xp"] > 0
    assert goblin["gold"] > 0


def test_goblin_is_alive():

    goblin = create_goblin()

    assert goblin["hp"] > 0


def test_goblin_is_dead():

    goblin = create_goblin()

    goblin["hp"] = 0

    assert goblin["hp"] <= 0


def test_goblin_king():

    boss = create_goblin_king()

    assert boss["name"] == "Goblin King"
    assert boss["hp"] == 100
    assert 10 <= boss["attack"] <= 15
    assert 6 <= boss["defence"] <= 9
    assert boss["boss"] is True

# COMBAT TESTS

def test_player_damage_is_at_least_one():

    player = create_player("TestHero")

    enemy = {
        "name": "Test Goblin",
        "hp": 30,
        "max_hp": 30,
        "attack": 7,
        "defence": 3
    }

    damage = calculate_player_damage(
        player,
        enemy
    )

    assert damage >= 1


def test_player_damage_does_not_exceed_attack():

    player = create_player("TestHero")

    enemy = {
        "name": "Test Goblin",
        "hp": 30,
        "max_hp": 30,
        "attack": 7,
        "defence": 3
    }

    damage = calculate_player_damage(
        player,
        enemy
    )

    assert damage <= player["attack"]


def test_enemy_damage_is_at_least_one():

    player = create_player("TestHero")

    enemy = {
        "name": "Test Goblin",
        "hp": 30,
        "max_hp": 30,
        "attack": 7,
        "defence": 3
    }

    damage = calculate_enemy_damage(
        player,
        enemy
    )

    assert damage >= 1

# LEVELING TESTS

def test_xp_required():

    assert xp_required(1) == 100
    assert xp_required(2) == 200
    assert xp_required(3) == 300


def test_level_up():

    player = create_player("TestHero")

    player["xp"] = 100

    check_level_up(player)

    assert player["level"] == 2
    assert player["max_hp"] == 120
    assert player["attack"] == 13
    assert player["defence"] == 7
    assert player["hp"] == 120


def test_no_level_up_without_enough_xp():

    player = create_player("TestHero")

    player["xp"] = 50

    check_level_up(player)

    assert player["level"] == 1
    assert player["max_hp"] == 100

