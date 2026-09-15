# EUCLIDICITY-RPG 
#### Video Demo: https://youtu.be/FiOOT42sSHY
#### Description:


 This is a simple Command Line Interface (CLI) RPG game that I have developed while attending the CS50 Introduction to Python Course.
 The Role-playing Game (RPG) is based on medieval era setting.
 I have included a lot of functions to make the progression of the game as a fantasy combat based storyline (kind of novel RPG ?).
 Following will be the explaination of each file and function included in the project-

In Project.py, I have a total of 4 functions including main where 
1. display_title = it displays the title of the game
2. get_menu_choice = it gets the choice in the menu from the player that corresponds with new game, load game or quit 
3. new_game = This prompts the user to a new game creation along with character creation with Hero's name. (this was all i could think of that time)
4. main = this incorporates the function and furthers the game into the story and village and if chosen quit, it displays the ending line.

In Player.py, I have implemented the core mechanics of the player settings such as name, HP (Hitpoints), attack, defence, xp (experience), gold, armour, helmet, weapon and finally level. These parameters develop along side the player as they defeat the dungeons and progress towards the ending. 
I have implemented the following functions as well-
1. rename_player = allows player to rename themselves
2. get_attack = it allows the attack power of the player to scale with different equipments and there is a base attack power regardless of the equipments.
3. get_defence = Similar to attack power, it focuses on the player defence and scales with the equipment and also has a base defence. Also has an extra feature that will completely block the enemies attack if the defence is higher.
4. equip_item = It equips the item the player purchases from the village merchant and it has a replacing feature that replaces the lower tier equipment with the higher one.
5. heal_player = Heals the player when not in combat to the maximum when selected rest at village
6. add_gold = adds the gold when killing enemies in the dungeon
7. add_xp = adds the experience same as add_gold for leveling the character
8. is_alive = placeholder for game logic to enusre player has health and is alive
9. display_defeat_message = Gives a defeat message after hp drops to zero
10. display_player = gives the current loadout of the character to ensure equipment and level is appropriate

Combat.py = The main gameplay mechanic of the whole game, it is based on the RNG (Random Number Generator) based idea I got from board games. I implemented using the Random library as i wanted it to be fair as possible. The armour and weapon add damage as a surplus/addition to te RNG based basic damage. 
We hav ethe following functions-
1. calculate_player_damage = it calculatest the damage the player deals to the enemies, the basic damage is random and weapons add extra damage
2. calculate_enemy_damage = Similar to above, it caluclates the damage dealt to the player by the enemies, except it is random and as defence imporves, player takes less damage and when using block, the damage may be nullified if the armour is high enough.
3. player_attack = It is the actual mechanic that employs the attack of the player encompassing the random attack plus the weapon's attack and is calcualted by the above function (calculate_player_damage). It also checks the enemies Hp so that it can progress the fight to the next enemy.
4. enemy_attack = It is similar to above and employs code of the attack of the enemy that has a predefined range for the RNG.
5. Combat = it is the main function that ensures the above functions are working in tandem and ensures proper hp and attack scaling for both the parties.

Enemies.py - Now on to the enemies of the game. I have included the basic fantasy enemies that are usually found in the dungeon such as goblins, skeletons, orcs, trolls and wyverns (lesser dragons).
Since i wanted the game to have levels to the progression, so i featured 5 levels of dungeons for each village level and there are further 5 levels of villages. Each dungeon instance has a distinct enemy type from the above 5 and every dungeon also has a five stage combat trial till the main boss of the dungeon that needs to be defeated to progress to the next level of the village.
The enemies give the player on defeat, xp and gold and also helps player in leveling.
These are the following functions that are implemented - 
1. create_goblin = this is the basic function for creating the enemy named goblin that has its own hp, attack and defence, same as the player hero. It also has set values for xp and gold that is given to the player after its defeat.
2. creat_goblin_king = This is the boss enemy of the dungeon and has the same specification such as its mob enemy (goblin) but all parameters have higher attack, defence, xp and gold. Also defeating the boss enemy opens the way to the next village and its dungeon.
3. _create_enemy = This is the main parent function under which multiple functions are nested that create different mob enemies for the progressive dungeon such as skeletons, orcs, trolls and wyverns with their own specifications such as hp, attack, defence, xp and gold. 
4. create_region_boss = Similar to above main function, it has nested functions that code the boss enemies of each dungeon in the vilages that are similar to goblin king and also have a boost in their specification leading from goblin king, skeleton lord, orc warlord, troll cheiftan, and final boss of all ancient wyvern.
5. is_alive = codes for enemy health till it reaches zero.
6. display_enemy = displays the enemy for each dungeon level and type.

Dungeon.py - Dungeons are the only place where the hero can fight the enemies to level up and thus in every village a dungeon exists and each dungeon has five stages with distinct enemy types-
1st stage = 1 mob enemy
2nd stage = 2 mob enemies
3rd stage = 3 mon enemies 
4th stage = 4 mob enemies
5th stage = Dungeon Boss 
The 1st to 3rd stage dont necessary require armour, equiptment or weapons in the first dungeon but the 4th and 5th stage require proper planning and equipments to challenge by the player.
1. give_reward = As the player defeats the enemy, they will receive the corresponding gold value that was placed on the enemy based on RNG.
2. dungeon_stage = Sets the stage for the dungeon in the region along with its boss and the mob enemies. It gets what village level the player is at and gets the mob and boss enemy for that level.
3. dungeon = It is the main function that codes the dungeon instance with its 5 stages and defeating the enemies advances the stages and killing the dungeon boss progresses the story and next village.

Leveling.py - It codes for the leveling feature of the game and it only has a single function = check_level_up that checks the levelup of the player through defeating the enemy and filling the xp for the next level.

Village.py - The village is like a menu of sorts for the player where a lot of functions from different files come together to give a resemblance of an actual medieval village with multiple places to help the hero. The village has multiple options as follows- 
* Dungeon - A village always has a dungeon as a threat to its existence that the hero needs to defeat.
* Merchant - This is where the player can buy equipment from the merchant to fight in the dungeon.
* Character - The player can check their current load out and level.
* Rest - The player can rest and allows their hero to regain their Hp back to full health.
* Rename Hero - just renaming the hero for a change of heart.
* Save game - saves the game.
* Story - The player can check the story progression to track their progress. 
* Travel - The main feature of the village that allows the player to travel to different villages and dungeons to challenge bosses for levels as the dungeons are progressively difficult. 
* Leave game - Ends the game.

Merchant.py - The merchant allows the player to buy items from them and challenge the dungeons, mainly boosting their attack and defence and furthermore there are tiers of equipments corresponding to the village level. Once a equipment of higher tier is bought, it replaces the lower tier one. Gold is needed to buy the equipment and a propmpt is displayed if there isnt enough gold. 

Equipment.py - This file contains all the types and tiers of equipments that will be availble at the merchant at different village levels and can be purchased for a certain amount of gold. Each equipment has a definite purpose, eg. weapons give you bonus attack, armour and helmet give you bonus defence.

Progression.py - This controls the prgression of the game and gives context for the vilage name, dungeon type, mob enemy and boss along with the story. It also gives the boss an intro of sorts.
The ensure_progression checks the unlocked region and displays the story and progression accordingly.

Save_load.py - There are 2 functions- 
1. save_game = This creates a json file for the player with the progression saved till played.
2. load_game = (Took a lot of time to understand how you load games) Retrieves the SAVE GAME json file. 
PS- i wanted to add this feature as during testing i got tired of going through everything again and again.

Story.py - This file contains the story context for the game (i am not good at story writing, anyone reading this, you can edit the story to match your fantasy). It also has some functions to ensure story progress, display the story and the scene and also display the story at the village. 

Test_project.py - Just a file with pytest of the functions i wanted to test to ensure the whole game was working and due to multiple things breaking a lot, i may have a lot of tests.


Anyone reading this very long read.me, I thank you for playing my first game.

