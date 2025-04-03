import random
import time
player_health = 1000
gold = 300
inventory = ["Shovel"]  # Start with a shovel
equipped_weapon = "Shovel"  # Start with a shovel equipped

weapons = { # list of the weapons
    "Shovel": 12,
    "Sword": 20
}

items = {
    "Health Potion": {"type": "heal", "amount": 30},  # Heals 30 HP
    "Cure Potion": {"type": "revive", "amount": 50}   # Revives a zombie ally with 50 HP
}

zombie_stats = [# enemy stats
    {"name": "evil corridor defender", "health": 30, "weapon": "hands", "damage": random.randint(10, 15)},
    {"name": "evil senior student", "health": 45, "weapon": "stick", "damage": random.randint(12, 18)},
    {"name": "evil teacher", "health": 60, "weapon": "enchanted ruler", "damage": random.randint(15, 20)},
    {"name": "Evil Mr Lessels", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(20, 25)},
    {"name": "Evil Mr Smith", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(20, 25)},
    {"name": "Evil Mr Stevenson", "health": 75, "weapon": "Boxing gloves", "damage": random.randint(20, 25)},
    {"name": "BOSS Mr Hunt", "health": 100, "weapon": "Mind control device", "damage": random.randint(20, 25)}
]


cured_zombies = []# this will store your zombies


def shop():
    global gold # gold info can be obtained from a different function

    items = {"Health Potion": 20,# items in the shop
             "Sword": 35,
             "cure potion": 45}

    while True:
        print("\n--- Shop ---")
        print(f"Your gold: {gold}")
        print("1. Buy Sword (35 gold)")
        print("2. Buy Health Potion (20 gold)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if gold >= 35: # checks if they have enough gold
                inventory.append("Sword")  # adds the sword to inventory
                gold -= 35 # removes the gold from them
                print("Sword added to your inventory.")
            else:
                print("You can't afford this")
            break # continues

        elif choice == "2":
            if gold >= 20:
                inventory.append("Health Potion")
                gold -= 20
                print("Health Potion added to your inventory.")
            else:
                print("You can't afford this")
            break

        if choice == "3":
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
            
def capture_zombie(zombie):
    global captured_zombies
    captured_zombies.append(zombie)
    print(f"You have captured the {zombie['name']}!")

def attack(enemy):
    damage = weapons[equipped_weapon] # creating a varible to use
    enemy["health"] -= damage # the maths of the code
    print(f"\nYou attack the {enemy['name']} with your {equipped_weapon} for {damage} damage!")# prints what you did

def zombie_attack(player_health, enemy):
    damage = enemy["damage"]  # Get the zombie's attack damage
    player_health -= damage  # Subtract the damage from the player's health
    print(f"\nThe {enemy['name']} attacks you for {damage} damage!")  # Print the zombie's attack
    return player_health

def story():
    while True:
        print()
        print("1. Go up the tower block")
        print("2. Go up the road")

        try:
            command = int(input("> "))# records the users choice
            if command == 1:
                story_tower()# makes them go to story1_1 of the game
            elif command == 2:
                story_road()# makes them go to story1_2 of the game
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")


def story_tower():
    zombie_weights = [1, 0, 0, 0, 0, 0, 0]  # 100% chance of encountering evil corridor defender
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]  # chooses a zombie depending on the chances
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")

    global player_health  # Make sure to modify the global player_health variable

    while enemy["health"] > 0 and player_health > 0:  # The game continues until either the zombie or the player dies
        print(f"\n{enemy['name']} health: {enemy['health']}")
        print(f"Your health: {player_health}")  # Show player's health
        print("1. Attack")
        
        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)  # Player attacks the zombie
                if enemy["health"] <= 0:  # If the zombie is defeated
                    print(f"You defeated the {enemy['name']}!")
 
                else:
                    # If the zombie is still alive, it attacks back
                    player_health = zombie_attack(player_health, enemy)  # Zombie attacks the player
                    if player_health <= 0:  # If player's health drops to 0 or below, the player dies
                        print("You have been defeated by the zombie!")
                        break  # End the fight if the player dies

            else:
                print("Invalid option.")
           
        except ValueError:
            print("Please enter a valid number.")

    if player_health > 0:
        # Post battle options using rules2()
        rules2()  # Call to show rules2 options

        try:
            command = int(input("> "))
            if command == 1:
                # Continue the game
                print("What would you like to do next?")
                print("1. Go up to the second floor")
                print("2. Go explore the first floor")
                next_choice = int(input("> "))
                if next_choice == 1:
                    story_second_floor()
                elif next_choice == 2:
                    story_first_floor()
                else:
                    print("Invalid choice. Returning to previous options.")
                    story_tower()  # Return to the tower if the choice is invalid

            elif command == 2:
                shop()  # Open the shop
            elif command == 3:
                see_inventory()  # Check the inventory
            elif command == 4:
                equip_weapon()  # Equip a weapon
            elif command == 5:
                print("Thanks for playing!")
                quit()
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")
            
def story_first_floor():
    zombie_weights = [0, 0, 0, 1, 0, 0, 0]  # 100% chance of encountering Mr lessels
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]  # chooses a zombie depending on the chances
    print(f"As you explore the first floor you encounter {enemy['name']}!")

    global player_health  # Make sure to modify the global player_health variable

    while enemy["health"] > 0 and player_health > 0:  # The game continues until either the zombie or the player dies
        print(f"\n{enemy['name']} Health: {enemy['health']}")
        print(f"Your health: {player_health}")  # Show player's health
        print("1. Attack")

        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)  # Player attacks the zombie
                if enemy["health"] <= 0:  # If the zombie is defeated
                    print(f"You defeated the {enemy['name']}!")
   
                else:
                    # If the zombie is still alive, it attacks back
                    player_health = zombie_attack(player_health, enemy)  # Zombie attacks the player brackets store info about player_health and enemy stats
                    if player_health <= 0:  # If player's health drops to 0 or below, the player dies
                        print("You have been defeated by the zombie!")
                        break  # End the fight if the player dies

            else:
                print("Invalid option.")
           
        except ValueError:
            print("Please enter a valid number.")
            
    if player_health > 0:
        # Post battle options using rules2()
        rules2()  # Call to show rules2 options

        try:
            command = int(input("> "))
            if command == 1:
                # Continue the game
                print("What would you like to do next?")
                print("1. Explore the Bridge")
                print("2. Explore 104 class")
                next_choice = int(input("> "))
                if next_choice == 1:
                    print("tester")
                elif next_choice == 2:
                    class_104()
                else:
                    print("Invalid choice. Returning to previous options.")
                    story_tower()  # Return to the tower if the choice is invalid

            elif command == 2:
                shop()  # Open the shop
            elif command == 3:
                see_inventory()  # Check the inventory
            elif command == 4:
                equip_weapon()  # Equip a weapon
            elif command == 5:
                print("Thanks for playing!")
                quit()
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")
            

def class_104():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1]  # 100% chance of encountering Mr lessels
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]  # chooses a zombie depending on the chances
    print(f"As you explore the first floor you encounter {enemy['name']}!")

    global player_health  # Make sure to modify the global player_health variable

    while enemy["health"] > 0 and player_health > 0:  # The game continues until either the zombie or the player dies
        print(f"\n{enemy['name']} Health: {enemy['health']}")
        print(f"Your health: {player_health}")  # Show player's health
        print("1. Attack")

        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)  # Player attacks the zombie
                if enemy["health"] <= 0:  # If the zombie is defeated
                    print(f"You defeated the {enemy['name']}!")
   
                else:
                    # If the zombie is still alive, it attacks back
                    player_health = zombie_attack(player_health, enemy)  # Zombie attacks the player brackets store info about player_health and enemy stats
                    if player_health <= 0:  # If player's health drops to 0 or below, the player dies
                        print("You have been defeated by the zombie!")
                        break  # End the fight if the player dies

            else:
                print("Invalid option.")
           
        except ValueError:
            print("Please enter a valid number.")
    if player_health > 0:
        FINAL_PART()

def story_second_floor():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0]  # 100% chance of encountering Mr Smith
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]  # chooses a zombie depending on the chances
    print(f"As you explore the first floor you encounter {enemy['name']}!")

    global player_health  # Make sure to modify the global player_health variable

    while enemy["health"] > 0 and player_health > 0:  # The game continues until either the zombie or the player dies
        print(f"\n{enemy['name']} Health: {enemy['health']}")
        print(f"Your health: {player_health}")  # Show player's health
        print("1. Attack")

        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)  # Player attacks the zombie
                if enemy["health"] <= 0:  # If the zombie is defeated
                    print(f"You defeated the {enemy['name']}!")
                  
                else:
                    # If the zombie is still alive, it attacks back
                    player_health = zombie_attack(player_health, enemy)  # Zombie attacks the player brackets store info about player_health and enemy stats
                    if player_health <= 0:  # If player's health drops to 0 or below, the player dies
                        print("You have been defeated by the zombie!")
                        break  # End the fight if the player dies
            elif command == 2:
                print("test code for now")  # Placeholder for using a cure or other item
                break
            else:
                print("Invalid option.")
           
        except ValueError:
            print("Please enter a valid number.")
           

def story_road():
    zombie_weights = [0, 7, 3, 0, 0, 0, 0]  # 70% of evil senior 30% evil teacher
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]  # chooses a zombie depending on the chances
    print(f"As you walk down the road you encounter a {enemy['name']}!")

    global player_health  # Make sure to modify the global player_health variable

    while enemy["health"] > 0 and player_health > 0:  # The game continues until either the zombie or the player dies
        print(f"\n{enemy['name']} health: {enemy['health']}")
        print(f"Your health: {player_health}")  # Show player's health
        print("1. Attack")

        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)  # Player attacks the zombie
                if enemy["health"] <= 0:  # If the zombie is defeated
                    print(f"You defeated the {enemy['name']}!")
                    break  # Exit the loop if the zombie is defeated
                else:
                    # If the zombie is still alive, it attacks back
                    player_health = zombie_attack(player_health, enemy)  # Zombie attacks the player brackets store info about player_health and enemy stats
                    if player_health <= 0:  # If player's health drops to 0 or below, the player dies
                        print("You have been defeated by the zombie!")
                        break  # End the fight if the player dies
            elif command == 2:
                print("test code for now")  # Placeholder for using a cure or other item
                break
            else:
                print("Invalid option.")
           
        except ValueError:
            print("Please enter a valid number.")


def FINAL_PART():
    # List of 5 puzzles with missing letters and hints
    puzzles = [
        {"clue": "Ki__", "answer": "kiwi", "hint": "It's a type of bird"},
        {"clue": "__ie_ce", "answer": "science", "hint": "A subject"},
        {"clue": "_o_n", "answer": "moon", "hint": "Something large found in the sky."},
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
