import random
import time
player_health = 100
gold = 300
inventory = ["Shovel"]  # Start with a shovel
equipped_weapon = "Shovel"  # Start with a shovel equipped

weapons = { # list of the weapons
    "Shovel": 1000,
    "Sword": 25,
    "Hammer": 32
}

words = ["charge", "peirce", "rush", "blitz","assault", "pounce", "stab", "ambush", "savage", "assault"]# if the user doesn't spell the word in 5 seconds they can't attack
words_defense = ["sheild", "protect", "block", "guard", "support", "stealth", "camouflage", "hidden", "invisable", "armour"]
words_heavy = ["hard", "crush", "slam", "smash", "impact", "thunder", "blow", "pound", "strike", "devastate"]
items = {
    "Health Potion": {"type": "heal", "amount": 30},  # Heals 30 HP
}

zombie_stats = [# enemy stats
        {"name": "evil corridor defender", "health": 30, "weapon": "hands", "damage": random.randint(4, 10)},
        {"name": "evil senior student", "health": 45, "weapon": "stick", "damage": random.randint(5, 10)},
        {"name": "evil teacher", "health": 60, "weapon": "enchanted ruler", "damage": random.randint(6, 10)},
        {"name": "Evil Mr Lessels", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Smith", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Stevenson", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "BOSS Mr Hunt", "health": 100, "weapon": "Mind control device", "damage": random.randint(15, 18)}
]


def shop():
    global gold # gold info can be obtained from a different function

    items = {"Health Potion": 20,# items in the shop
             "Sword": 35,
             "Hammer": 45}

    while True:
        print("\n--- Shop ---")
        print(f"Your gold: {gold}")
        print("1. Buy Sword (25 gold) - deals 25 damage")
        print("2. Buy Hammer (45 gold) - 20% chance dealing more damgae, deals 40 damage")
        print("3. Buy Health Potion (20 gold) - heals half of your health")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if gold >= 25: # checks if they have enough gold
                inventory.append("Sword")  # adds the sword to inventory
                gold -= 25 # removes the gold from them
                print("Sword added to your inventory.")
            else:
                print("You can't afford this")
            break # continues

        elif choice == "2":
            if gold >= 45:
                inventory.append("Hammer")
                gold -= 45
                print("Hammer added to your inventory.")
            else:
                print("You can't afford this")
            break
        
        elif choice == "3":
            if gold >= 20:
                inventory.append("Health Potion")
                gold -= 20
                print("Health Potion added to your inventory.")
            else:
                print("You can't afford this")
            break

        if choice == "4":
            print("Goodbye!")
            break

        else: # invalid inputs
            print("Invalid option. Try again.")

def equip_weapon():
    global equipped_weapon

    weapons_in_inventory = [w for w in inventory if w in weapons]# contains weapons that are in inventory
    items_in_inventory = [i for i in inventory if i in items]# contains items that are in inventory

    print("\nYour weapons and items:")
    options = [f"Equip {w} (Damage: {weapons[w]})" for w in weapons_in_inventory] + [f"Use {i}" for i in items_in_inventory]
    # this prints use/equip weapons and items in your inventory
    for idx, option in enumerate(options, 1):# makes sure that item is numbered correctly
        print(f"{idx}. {option}")# prints the number and then the item/weapon

    try:
        choice = int(input("Choose a weapon/item: ")) - 1 # -1 makes it more user friendly list starts at 0
       
        if 0 <= choice < len(weapons_in_inventory):# this ensures that choice is a valid weapon selection
            equipped_weapon = weapons_in_inventory[choice]# changes weapon
            print(f"You equipped the {equipped_weapon}!")# prints the equipped weapon
        elif choice < len(options):
            use_item(items_in_inventory[choice - len(weapons_in_inventory)])# this checks if its an item not a weapon
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def use_item(item):# it stores what item was used
    if item == "Health Potion":# checks if health potion was used
        print("You used a Health Potion for 50 health!")

    else:
        print("Item not recognized.")# invalid choice


def see_inventory():
    print("\nYour inventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}") # makes everything in lines so it's easier to read
    else:
        print("Your inventory is empty.")

    print(f"\nCurrently equipped weapon: {equipped_weapon} (Damage: {weapons[equipped_weapon]})")# prints the weapon they are using and the damage


def rules(): # basic rules the only prints at the start of the game
    print("Welcome to my game!")
    print("Your goal is to escape school.")
    print("Mr Hutt has turned everyone evil with his mind control device.")
    print("Defeat Mr Hutt and destroy his mind control device to save the school.")
    print("You start with a shovel as your weapon.")
    print("You can buy items from the in-game shop.")
    print("You start with 30 gold and can earn more by fighting.")
    print("Fight the evil, cure them, and buy weapons to survive.")
    first_option()


def rules2():# basic print code
    print("\n--- Survival Game ---")
    print("1. Continue with the game")
    print("2. Enter the shop")
    print("3. Check your inventory")
    print("4. Equip a weapon")
    print("5. Quit")


def first_option():
    global gold

    while True:
        rules2()# prints rules2 and then goes back to the code
        command = input("> ").strip()# removes spaces in userinput answer

        if command == "1":
            story()
        elif command == "2":
            shop()
        elif command == "3":
            print(f"\nYour current gold: {gold}")# reminds then how much gold they have
            see_inventory()
        elif command == "4":
            equip_weapon()
        elif command == "5":
            print("Thanks for playing!")
            quit()
        else:
            print("\nInvalid command. Try again.")
def apply_extra_damage(damage):

    if equipped_weapon == "Hammer":
        if random.random() < 0.8:  # 20% chance to apply extra damage
            extra_damage = damage * 0.2  # 20% of the base damage
            damage += extra_damage  # Add extra damage to the total damage
            print(f"Your hammer does extra damage! ({extra_damage} added)")
    return damage

def attack(enemy):
    damage = weapons[equipped_weapon] # creating a varible to use
    damage = apply_extra_damage(damage)
    enemy["health"] -= damage # the maths of the code
    print(f"\nYou attack the {enemy['name']} with your {equipped_weapon} for {damage} damage!")# prints what you did

def zombie_attack(player_health, enemy):
    damage = enemy["damage"]  # Get the zombie's attack damage
    player_health -= damage  # Subtract the damage from the player's health
    print(f"\nThe {enemy['name']} attacks you for {damage} damage!")  # Print the zombie's attack
    return player_health
def heavy_attack(enemy):

    miss_chance = 0.5  # 50% chance to miss
    if random.random() < miss_chance:
        print("You swing your weapon with maximum force but the enemy predicted your attack...")
        return 0  # No damage if it misses
    else:
        damage = weapons[equipped_weapon] * 2  # Double damage for heavy attack
        damage = apply_extra_damage(damage)
        enemy["health"] -= damage
        print(f"You deal {damage} damage to the {enemy['name']} with your heavy attack!")
        return damage
def defense(enemy):
    global player_health
    original_damage = enemy["damage"]  # Zombie's original damage
    absorbed_damage = original_damage * 0.7  # Absorbed 70% of the damage
    reflected_damage = original_damage * 0.3  # Reflected 30% of the damage

    reflected_damage = apply_extra_damage(reflected_damage)
    player_health -= absorbed_damage # Player absorbs 70% of the damage
    
    enemy["health"] -= reflected_damage# Reflects 30% of the damage to the enemy
    print(f"You absorb {absorbed_damage:.2f} damage and reflect {reflected_damage:.2f} damage back to the {enemy['name']}!")
    return player_health
def handle_battle(enemy):
    print("You must spell out one of the attacks if spelt incorrectly you wont't be able to attack:")
    print("Choose Your opition")
    print("1. Attack")
    print("2. Defend")
    print("3. Heavy Attack")
    
    try:
        action = input("> ").lower()

        if action == "attack":  # If the player chooses "attack"
            if spelling_challenge("attack") == True:  # Call spelling challenge for attack
                attack(enemy)  # Perform the attack action
                if enemy["health"] <= 0:
                    print(f"You defeated the {enemy['name']}!")
                    return
            else:
                print("You failed to perform the attack!")
                
        elif action == "defend":  # If the player chooses "defend"
            if spelling_challenge("defend") == True:  # Call spelling challenge for defend
                defense(enemy)  # Perform the defend action
                if enemy["health"] <= 0:
                    print(f"You defeated the {enemy['name']} by reflecting damage!")
                    return
            else:
                print("You failed to defend!")
                
        elif action == "heavy attack":  # If the player chooses "heavy"
            if spelling_challenge("heavy attack") == True:  # Call spelling challenge for heavy attack
                heavy_attack(enemy)  # Perform the heavy attack action
                if enemy["health"] <= 0:
                    print(f"You defeated the {enemy['name']} with a heavy attack!")
                    return
            else:
                print("You failed to perform the heavy attack!")

        else:
            print("Invalid action! Choose 'attack', 'defend', or 'heavy'.")
            handle_battle(enemy)  # Prompt again if invalid input

    except ValueError:
        print("Please enter a valid input.")
                    
def spelling_challenge(action_type):
    # Choose the correct list based on the action type
    if action_type == "attack":
        word_list = words
    elif action_type == "defend":
        word_list = words_defense
    elif action_type == "heavy attack":
        word_list = words_heavy
    
    # Choose a random word from the selected list
    word = random.choice(word_list)

    print(f"\nYou must spell the following word to {action_type}!")
    print("Spell the word within 5 seconds to succeed.")
    print(f"Word: {word}")

    start_time = time.time()  # Record the start time
    user_input = input("Type the word: ")

    elapsed_time = time.time() - start_time  # Calculate time elapsed

    if elapsed_time > 5:
        print("\nYou ran out of time! You lose your turn.")
        return False  # Player failed to spell the word within time limit
    elif user_input.lower() == word:
        print(f"\nCorrect! You successfully used {action_type}!")
        return True  # Player spelled the word correctly
    else:
        print("\nIncorrect spelling! You lose your turn.")
        return False  # Player spelled the word incorrectly
def story():
    while True:
        print()
        print("1. Go up the tower block")
        print("2. Go up the road")

        try:
            command = int(input("> "))# records the users choice
            if command == 1:
                tower_block()# makes them go to ... of the game
            elif command == 2:
                road_explore()# makes them go to ... of the game
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")

def tower_block():
    zombie_weights = [1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore first floor")
                    print("2. go up the second floor")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_first()
                    elif next_choice== 2:
                        second()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def explore_first():
    zombie_weights = [0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore halls")
                    print("2. explore the bridge")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_halls()
                    elif next_choice== 2:
                        explore_bridge()
                    else:
                        print("Invalid choice. Returning to previous options.")
            except ValueError:
                print("Please enter a valid number.")
def explore_halls():
    zombie_weights = [1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore elevator")
                    print("2. explore classes")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_elevator()
                    elif next_choice== 2:
                        explore_class()
                    else:
                        print("Invalid choice. Returning to previous options.")
            except ValueError:
                print("Please enter a valid number.")
def explore_bridge():
    zombie_weights = [0, 0, 0, 1, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore 'STAFF ONLY' room")
                    print("2. explore under the bridge")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_staff()
                    elif next_choice== 2:
                        explore_downstairs()
                    else:
                        print("Invalid choice. Returning to previous options.")
            except ValueError:
                print("Please enter a valid number.")
def explore_staff():
    print("As you start walking towards the staff only room, you hear a lot of noise")
    print("turn around?")
def explore_downstairs():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As go downstairs you encounter {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    FINAL_PART()
                else:
                    print("Invalid choice. Returning to previous options.")
            except ValueError:
                    print("Please enter a valid number.")


def explore_elevator():
    ("this is the bad ending")
def explore_class():
    zombie_weights = [0, 2, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("You walk into a class")
                    FINAL_PART()
                else:
                    print("Invalid choice. Returning to previous options.")
            except ValueError:
                print("Please enter a valid number.")
def second():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore second floor")
                    print("2. go up the third floor")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_second()
                    elif next_choice== 2:
                        explore_third()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def explore_second():
    zombie_weights = [0, 0, 0, 0, 0, 1, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. ask a student what to do")
                    print("2. go up the elevator")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        student()
                    elif next_choice== 2:
                        explore_elevator()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def student():
    while True:
        try:
            print("The student tells you what you need to do to save wc is to go to the libary and thats where the mind control device is")
            print("Do you trust the student?")
            print("1. go to the libary")
            print("2. go up the elevator")
            next_choice = int(input("> "))
            if next_choice == 1:
                libary()
            elif next_choice == 2:
                print("you dont listen to him")
                print("and go to the third floor")
                explore_third()
            else:
                print("Invalid choice. Returning to previous options.")
                tower_block()
        except ValueError:
            print("Please enter a valid number.")

def libary():
    print("betryal ending")
def explore_third():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore tools room")
                    print("2. go up the elevator")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_tools()
                    elif next_choice== 2:
                        explore_elevator()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def explore_tools():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. Go to the mysterious room")
                    print("2. go up to fourth floor")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        mystery_room()
                    elif next_choice== 2:
                        fourth_floor()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def mystery_room():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As go inside the mystery room you see {enemy['name']} looking at the mind control device")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    FINAL_PART()
                else:
                    print("Invalid choice. Returning to previous options.")
            except ValueError:
                    print("Please enter a valid number.")
def fourth_floor():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. Use your key to go inside the loud room")
                    print("2. go up on top of tower block")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        weird_ending()
                    elif next_choice== 2:
                        top_floor()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")
def top_floor():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"Your standing on the top of the tower block a strong gust of wind hits you, you sense the final battle awaits, {enemy['name']} comes towards you")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    FINAL_PART()
                else:
                    print("Invalid choice. Returning to previous options.")
            except ValueError:
                    print("Please enter a valid number.")

def weird_ending():
    print("You walk into the loud room start partying with the people")
def road_explore():
    zombie_weights = [1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. Use your key to go inside the loud room")
                    print("2. go up on top of tower block")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        weird_ending()
                    elif next_choice== 2:
                        top_floor()
                    else:
                        print("Invalid choice. Returning to previous options.")
                        tower_block()
            except ValueError:
                print("Please enter a valid number.")

def LOSE_PART():
    print("losing fuinction")


def FINAL_PART():
    print("you defeated the boss, mr hunt to defuse the mind controlling device you must solve a puzzle")
    # List of 5 puzzles with missing letters and hints
    puzzles = [
        {"clue": "Ki__", "answer": "kiwi", "hint": "It's a type of bird"},
        {"clue": "_____ce", "answer": "science", "hint": "A subject"},
        {"clue": "___n", "answer": "moon", "hint": "Something large found in the sky."},
        {"clue": "_r__on  _r__t", "answer": "dragon fruit", "hint": "A fruit commonly in asia."},
        {"clue": "o______n", "answer": "obsidian", "hint": "Volcano"}
    ]
   
    for level in range(1, 6):  # Loop through levels 1 to 5
        # Set the time limit for each level
        if level == 1:
            max_time = 30  # Level 1 = 30 seconds
        elif level == 2:
            max_time = 25  # Level 2 = 25 seconds
        elif level == 3:
            max_time = 20  # Level 3 = 20 seconds
        elif level == 4:
            max_time = 15  # Level 4 = 15 seconds
        elif level == 5:
            max_time = 10  # Level 5 = 10 seconds
       
        puzzle = puzzles[level - 1]  # Get the current puzzle
       
        print(f"\n--- Level {level} ---")
        print(f"Clue: Fill in the missing letters for this word.")
        print(f"Puzzle: {puzzle['clue']}")
        print(f"Hint: {puzzle['hint']}")
       
        start_time = time.time()  # Start the timer
        user_answer = input(f"You have {max_time} seconds. Enter your answer: ").lower()
       
        # Check if the time has exceeded the max time allowed
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"Time's up! You took too long to answer. ({max_time} seconds allowed)")
            break
       
        # Check if the answer is correct
        if user_answer == puzzle["answer"]:
            print(f"Correct! The word was '{puzzle['answer']}'")
        else:
            print(f"Incorrect! The correct answer was '{puzzle['answer']}'")
            break  # End the game after one wrong answer (optional)

        # Check if the player completed all levels
        if level == 5:
            print("\nCongratulations! You've completed all levels and defused the mind-control device!")

   
rules()
