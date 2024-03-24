import random
import json
from django.conf import settings
from pathlib import Path

def load_data():
    filepath = Path(settings.BASE_DIR) / 'app' / 'data.json'  
    with open(filepath, "r") as file:
        content = json.load(file)
    return content

def generate_character(data):
    character = {
        "Race": random.choice(data["races"]),
        "Class": random.choice(data["classes"]),
        "Backpack": random.choice(data["backpacks"]),
        "Second Class Permission": random.choice(data["second_class_permission"]),
        "Second Class": [None],
        "Curses": ["None"],
        "Boon": ["None"],
        "Standing Stone": random.choice(data["standing_stones"]),
        "Starting Location": random.choice(data["starting_locations"]),
        "Main Quest": random.choice(data["main_quests"]),
        "Side Quest": random.choice([quest for quest in data["main_quests"] if quest != "Main Quest"]),
        "Skills": random.sample(data["skills"], 5)
    }
    
    if character["Second Class Permission"] == "Yes! take two curses and a second class!":
        character["Second Class"] = random.choice([cls for cls in data["classes"] if cls != character["Class"]])
        
        # Select 2 curses
        character["Curses"] = random.sample(list(data["curses"].keys()), k=2)
        shard_count = sum(data["curses"][curse] for curse in character["Curses"])
        # Allocate boon if extra shards
        if shard_count > 2:
            character["Boon"] = random.choice(list(data["boons"].keys()))
    # If permission is "Nope!", no curses and no boons are allocated

    # Ensures Main Quest and Side Quest are different
    while character["Side Quest"] == character["Main Quest"]:
        character["Side Quest"] = random.choice([quest for quest in data["main_quests"] if quest != character["Main Quest"]])

    return character


def print_character(character):
    for attribute, value in character.items():
        if isinstance(value, list) and not value:
            print(f"{attribute}: None")
        elif isinstance(value, list):
            print(f"{attribute}: {', '.join(value)}")
        else:
            print(f"{attribute}: {value}")
