class Character:
    """Base class for anyone who can fight: shared stats and combat actions."""

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        # Defense softens incoming damage, but every hit does at least 1
        damage = max(1, amount - self.defense)
        self.hp = max(0, self.hp - damage)
        return damage

    def basic_attack(self, target):
        damage = target.take_damage(self.attack)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        return damage


class Item:
    """Base class for anything the player can carry and use."""

    def __init__(self, name):
        self.name = name

    def use(self, player):
        """Override in subclasses to define what using this item does."""
        print("Nothing happens.")


class Potion(Item):
    """A consumable that restores hp."""

    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def use(self, player):
        healed = min(self.heal_amount, player.max_hp - player.hp)
        player.hp += healed
        print(f"{player.name} uses {self.name} and recovers {healed} HP.")


class Inventory:
    """Holds a player's items."""

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item.name} added to inventory.")

    def show(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("Inventory:")
        for i, item in enumerate(self.items, start=1):
            print(f"  {i}. {item.name}")

    def use(self, index, player):
        """Use the item at the given 1-based position, then remove it."""
        if index < 1 or index > len(self.items):
            print("Invalid item.")
            return
        item = self.items.pop(index - 1)
        item.use(player)


class Player(Character):
    """The character controlled by the person playing."""

    def __init__(self, name, hp=30, attack=8, defense=2):
        super().__init__(name, hp, attack, defense)
        self.level = 1
        self.xp = 0
        self.inventory = Inventory()

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP.")
        while self.xp >= self.xp_to_next_level():
            self.level_up()

    def xp_to_next_level(self):
        return self.level * 20

    def level_up(self):
        self.xp -= self.xp_to_next_level()
        self.level += 1
        self.max_hp += 5
        self.hp = self.max_hp  # level-ups fully heal you as a reward
        self.attack += 2
        self.defense += 1
        print(f"{self.name} leveled up to level {self.level}! "
              f"(HP {self.max_hp}, Attack {self.attack}, Defense {self.defense})")


class Enemy(Character):
    """A monster the player fights."""

    def __init__(self, name, hp, attack, defense, xp_reward):
        super().__init__(name, hp, attack, defense)
        self.xp_reward = xp_reward


def battle(player, enemy):
    """A turn-based fight: player and enemy trade attacks until one falls."""
    print(f"\nA wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp}  |  "
              f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        choice = input("1) Attack  2) Use item\n> ").strip()

        if choice == "2":
            player.inventory.show()
            pick = input("Which item number? (Enter to cancel) ").strip()
            if pick.isdigit():
                player.inventory.use(int(pick), player)
            else:
                print(f"{player.name} hesitates and wastes the turn.")
        else:
            player.basic_attack(enemy)

        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            player.gain_xp(enemy.xp_reward)
            return True

        enemy.basic_attack(player)

        if not player.is_alive():
            print(f"{player.name} has been defeated...")
            return False

    return player.is_alive()


SCENES = {
    "start": {
        "text": (
            "You wake up at the edge of Fern Hollow with no memory of how you got here.\n"
            "A dirt path splits: one way leads into a dark forest, the other toward a\n"
            "faint plume of smoke on a hill.\n"
            "  1) Head into the forest\n"
            "  2) Walk toward the smoke"
        ),
        "options": {"1": "forest", "2": "hilltop"},
    },
    "forest": {
        "text": "The trees close in overhead. Something growls in the undergrowth ahead of you.",
        "battle": "goblin",
        "next": "clearing",
    },
    "clearing": {
        "text": (
            "Beyond the trees, you find a quiet clearing with a small shrine.\n"
            "  1) Continue toward the hill"
        ),
        "options": {"1": "hilltop"},
    },
    "hilltop": {
        "text": "At the top of the hill, a second goblin guards a burnt-out campfire.",
        "battle": "goblin",
        "next": "ending",
    },
    "ending": {
        "text": "With the path clear, you spot a village in the distance. Your journey continues another day.",
        "options": {},
    },
}


def make_enemy(kind):
    """A fresh enemy for a scene -- a new object each time, so no battle remembers the last one."""
    if kind == "goblin":
        return Enemy("Goblin", hp=15, attack=5, defense=1, xp_reward=10)
    raise ValueError(f"Unknown enemy type: {kind}")


def play_game():
    hero = Player("Hero")
    hero.inventory.add(Potion("Health Potion", heal_amount=15))

    scene_key = "start"
    while hero.is_alive():
        scene = SCENES[scene_key]
        print(f"\n{scene['text']}")

        if "battle" in scene:
            enemy = make_enemy(scene["battle"])
            if not battle(hero, enemy):
                break
            scene_key = scene["next"]
            continue

        options = scene["options"]
        if not options:
            break  # no options left -- the story has ended

        choice = None
        while choice not in options:
            choice = input("> ").strip()
        scene_key = options[choice]

    if hero.is_alive():
        print(f"\n{hero.name} made it through, level {hero.level}.")
    else:
        print(f"\n{hero.name}'s journey ends here.")


def main():
    play_game()


if __name__ == "__main__":
    main()