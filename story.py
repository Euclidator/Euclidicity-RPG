STORY_SCENES = {
    0: ("THE BEGINNING", [
        "For generations, Euclidicity was protected by the Crystal Compass.",
        "Tonight, its light has gone dark, and goblins have gathered beneath "
        "the village.",
        "Find the source of the darkness and restore the compass.",
    ]),
    1: ("THE GOBLIN'S SHARD", [
        "The Goblin King guarded the first compass shard beneath the Beginner "
        "Dungeon.",
        "With the shard reclaimed, a path opens toward the northern crypts.",
    ]),
    2: ("BONEWATCH", [
        "The skeletons of Bonewatch Village rise whenever the compass flickers.",
        "Their lord carries another shard, hidden in the Skeleton Crypt.",
    ]),
    3: ("IRON AND ASH", [
        "The next shard lies in an orc stronghold beyond Ironclad Village.",
        "The Orc Warlord is forging the shards into a weapon of war.",
    ]),
    4: ("THE DEEP CAVERNS", [
        "The weapon's power has awakened the trolls beneath Emberfall Village.",
        "Their chieftain guards the fourth shard in caverns older than memory.",
    ]),
    5: ("THE WYVERN'S PEAK", [
        "The final shard was carried into the clouds by an ancient wyvern.",
        "Climb Skyreach Peak, defeat the dragon, and restore the Crystal Compass.",
    ]),
    6: ("A NEW DAWN", [
        "The Crystal Compass shines again, and the darkness over Euclidicity "
        "breaks apart.",
        "Villages across the realm celebrate the hero who reunited the shards.",
        "The road ahead is open. This is only the beginning of your adventure.",
    ]),
}


def ensure_story_progress(player):
    progress = player.get("story_progress", 0)
    if not isinstance(progress, int):
        progress = 0
    player["story_progress"] = max(0, min(progress, max(STORY_SCENES)))
    return player["story_progress"]


def show_scene(player, scene):
    ensure_story_progress(player)
    title, lines = STORY_SCENES[scene]
    print()
    print("=" * 40)
    print(f"          {title}")
    print("=" * 40)
    for line in lines:
        print(line)
        input("Press Enter to continue...")


def start_story(player):
    ensure_story_progress(player)
    show_scene(player, 0)
    player["story_progress"] = max(player["story_progress"], 1)


def advance_story(player, progress):
    ensure_story_progress(player)
    if progress <= player["story_progress"]:
        return
    scene = min(progress, max(STORY_SCENES))
    player["story_progress"] = scene
    show_scene(player, scene)


def story_menu(player):
    ensure_story_progress(player)
    while True:
        print()
        print("=" * 40)
        print("             STORY")
        print("=" * 40)
        for scene in range(player["story_progress"] + 1):
            print(f"{scene + 1}. {STORY_SCENES[scene][0]}")
        print(f"{player['story_progress'] + 2}. Leave")

        choice = input("> ").strip()
        if not choice.isdigit():
            print("Invalid choice.")
            continue
        selected = int(choice) - 1
        if 0 <= selected <= player["story_progress"]:
            show_scene(player, selected)
        elif selected == player["story_progress"] + 1:
            return
        else:
            print("Invalid choice.")
