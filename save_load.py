import json

from progression import ensure_progress
from story import ensure_story_progress

SAVE_FILE = "savegame.json"


def save_game(player):

    try:

        with open(SAVE_FILE, "w") as file:
            json.dump(player, file, indent=4)

        print()
        print("Game saved successfully.")

    except OSError:
        print("Unable to save the game.")


def load_game():

    try:

        with open(SAVE_FILE, "r") as file:
            player = json.load(file)

        ensure_progress(player)
        ensure_story_progress(player)
        print()
        print("Game loaded successfully.")

        return player

    except (OSError, json.JSONDecodeError):

        print()
        print("No valid save file was found.")

        return None