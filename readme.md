
# Modded Skyrim Character Randomizer

## Overview
A Character Randomizer Built with Django for my own Modded Skyrim setup. Generates new starting combinations for hardcore permadeath playthroughs. I've also find it helps me discover playstyles and combinations that delightfully get me out of my comfort zone... finally with a click of a button!

## Getting Started

- Simply visit [> The live app <](https://realmlorkhanchargen-9469f78ddf76.herokuapp.com) and click roll!

##### Note: Requires both Dawnguard and Dragonborn DLCs.

- Currently the parameters that are published are for my specific load order, however in the future I plan to integrate more customization for you to adapt to your own setup. The following quest mods this can cover are listed below:

###### Vanilla Quests:
    Main Quest (Destroy Aldiun)
    Civil War (Imperial)
    Civil War (Stormcloaks)
    Join Dawnguard (Dawnguard DLC)
    Join Volkihar (Dawnguard DLC)
    Solstheim Island (Dragonborn DLC)
    College of Winterhold
    The Companions
    Dark Brotherhood
    Thieves Guild
    The Bards College

###### Modded Quests:
    Legacy of the Dragonborn
    Helgen Reborn
    Conquest of Skyrim
    Project AHO
    Vigilant
    Unslaad
    Identity Crisis
    Wheels of Lull
    Tools of Kagrenac
    Sirenroot
    Glenmoril

###### Planned / Considered implementations:
    - Allow users to upload their own modlist and use to randomize said quests.
    - Allow users to set how many skills, quests, and other details with the calculations.
    - Bug Fixes (ie, this can random conflicting questlines in its current state).
    - Potentially expand this to other alternative starting mods.
    

### Misc:

- Built with Python 3.12 and Django 3
- Uses an AJAX script to update character information without reloading the page.


