import random
import time

player_health = 100
gold = 15
inventory = ["Shovel"]  # Start with a shovel
equipped_weapon = "Shovel"  # Start with a shovel equipped

weapons = { # list of the weapons
    "Shovel": 12,
    "Sword": 22,
    "Hammer": 28
}
items = {
    "Health Potion": {"type": "heal", "amount": 40},  # Heals 40 HP
}
# scambled words it is called synonyms because i had a synomyms game before but i changed it because it was easy
synonyms = {
    "rbastkefa": ["breakfast","morning"],
    "egam": ["game","fun"],
    "tsrogn": ["strong","gym"],
    "artsm": ["smart","brain"],
    "braev": ["brave","bold"],
    "bgi": ["big","no clue"],
    "llsma": ["small","no clue"],
    "eholl": ["hello","no clue"],
    "unnfy": ["funny","emotion"],
    "onwdwi": ["window","see through"],
    "ptopal": ["laptop","everyday object for school"],
    "lohcso": ["school","big building"],
    "gnadro": ["dragon","not real"],
    "tfrlyetbu": ["butterfly","can fly"],
    "argiut": ["guitar","makes sound"],
    "zleuzp": ["puzzle","lots of pieces"],
    "rldwo": ["world", "no clue"],
    "tsoac": ["coast", "beach"],
    "noitcelfer": ["reflection", "you"],
    "nalp": ["plan", "stratergy"],
    "dnlno": ["london", "Uk"],
    "tacilap": ["capital", "city government"],
    "necbh": ["bench", "convient"],
    "ira": ["air", "very small"],
    "repag": ["grape", "fruit"],
    "aphr": ["harp", "instrument"],
    "rpco": ["crop", "harvest"],
    "ows": ["sow", "plant seeds"],
    "sgum": ["gums", "teeth"],
    "kcediw": ["wicked", "evil"],
    "saix": ["axis", "maths"],
    "ohtguor": ["through", "passageway"],
    "feer": ["free", "no clue"],
    "sadpnetn": ["pendants", "neck jewelry"],
    "lbel": ["bell", "loud"],
    "clfyut": ["flycult", "circle"],
    "eshor": ["horse", "animal"],
    "darc": ["card", "game"],
    "ekam": ["make", "create"],
    "acer": ["race", "fast"],
    "aren": ["near", "close"],
    "gninrael": ["learning", "school"],
    "xetnoisen": ["extension", "longer"],
    "tac": ["cat", "pet"],
    "odg": ["dog", "pet"],
    "okbo": ["book", "read"],
    "acelp": ["place", "location"],
    "emit": ["time", "clock"],
    "kgnwiro": ["working", "job"],
    "olvar": ["valor", "bravery"],
    "edne": ["need", "want"],
    "tkal": ["talk", "use your voice"],
    "odog": ["good", "well done"],
    "tabh": ["bath", "warm water"],
    "lesep": ["sleep", "night time activity"],
    "onseh": ["hones", "sharpens"],
    "elttob": ["bottle", "holds liquid"],
    "crema": ["cream", "goes on dessert"],
    "lciko": ["click", "mouse sound"],
    "yrarlbi": ["library", "books"],
    "eamt": ["team", "group work"],
    "nateleph": ["elephant", "big animal"],
    "clisoa": ["social", "people things"],
    "airn": ["rain", "comes from clouds"],
    "rca": ["car", "drives"],
    "plape": ["apple", "fruit"],
    "sesunihn": ["sunshine", "bright day"],
    "meusum": ["museum", "exhibits"],
    "tanem": ["meant", "intended"],
    "lenpa": ["panel", "flat section"],

}


zombie_stats = [# enemy stats how much hp and damage they do
        {"name": "Evil corridor defender", "health": 30, "weapon": "hands", "damage": random.randint(6, 10)},
        {"name": "Evil senior student", "health": 45, "weapon": "stick", "damage": random.randint(7, 10)},
        {"name": "Evil teacher", "health": 55, "weapon": "enchanted ruler", "damage": random.randint(8, 10)},
        {"name": "Evil Mr Lessels", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Smith", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Stevenson", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Elvis", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "BOSS Mr Hunt", "health": 100, "weapon": "Mind control device", "damage": random.randint(15, 18)}
]

zombie_stats2 = [# second set of mobs
        {"name": "Evil corridor defender", "health": 30, "weapon": "hands", "damage": random.randint(4, 10)},
        {"name": "Evil senior student", "health": 45, "weapon": "stick", "damage": random.randint(5, 10)},
        {"name": "Evil teacher", "health": 55, "weapon": "enchanted ruler", "damage": random.randint(6, 10)},
        {"name": "Evil Mr Lessels", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Smith", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Evil Mr Stevenson", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "Elvis", "health": 64, "weapon": "Boxing gloves", "damage": random.randint(10, 12)},
        {"name": "BOSS Mr Hunt", "health": 100, "weapon": "Mind control device", "damage": random.randint(15, 18)}
]




def shop():# the shop function where you can buy items
    global gold # gold can be obtained from a different function

    items = {"Health Potion": 20,# items in the shop
             "Sword": 35,
             "Hammer": 45}

    while True:# this loops incase they typo
        print("\n--- Shop ---")# shop
        print(f"Your gold: {gold}")
        print("1. Buy Sword (25 gold) - deals 25 damage")
        print("2. Buy Hammer (35 gold) - 25% chance dealing more damgae, deals 32 damage")
        print("3. Buy Health Potion (15 gold) - heals half of your health")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if gold >= 25: # checks if they have enough gold
                inventory.append("Sword")  # adds the sword to inventory
                gold -= 25 # removes the gold from them
                print("Sword added to your inventory.")
                print("make sure you equip it")
               
            else:
                print("You can't afford this")
            break # continues

        elif choice == "2":# the same thing above
            if gold >= 35:
                inventory.append("Hammer")
                gold -= 35
                print("Hammer added to your inventory.")
                print("make sure you equip it")
            else:
                print("You can't afford this")
            break
       
        elif choice == "3":
            if gold >= 15:
                inventory.append("Health Potion")
                gold -= 15
                print("Health Potion added to your inventory.")
                print("make sure you use it")
            else:
                print("You can't afford this")
            break

        if choice == "4":
            print("Goodbye!")
            break

        else: # invalid inputs
            print("Invalid option. Try again.")

def equip_weapon():# this function removes the equiped weapon and replaces it for a different weapon
    global equipped_weapon# this is a varible that tells the game what weapon you have equip

    weapons_in_inventory = [w for w in inventory if w in weapons]# contains weapons that are in inventory w means weapons
    items_in_inventory = [i for i in inventory if i in items]# contains items that are in inventory i means items

    print("\nYour weapons and items:")
    options = [f"Equip {w} (Damage: {weapons[w]})" for w in weapons_in_inventory] + [f"Use {i}" for i in items_in_inventory]# prints equip weapon and the damage if its in inventory
    # this prints use/equip weapons and items in your inventory
    for idx, option in enumerate(options, 1):# makes sure that item is numbered correctly
        print(f"{idx}. {option}")# prints the number and then the item/weapon

    try:
        choice = int(input("Choose a weapon/item: ")) - 1 # -1 makes it more user friendly list starts at 0
       
        if 0 <= choice < len(weapons_in_inventory):# this ensures that choice is a valid weapon selection
            equipped_weapon = weapons_in_inventory[choice]# changes weapon
            print(f"You equipped the {equipped_weapon}!")# prints the equipped weapon
        elif choice < len(options):# if choice is higher than the number of weaons there are it will detect that it is an item
            use_item(items_in_inventory[choice - len(weapons_in_inventory)])# this checks if its an item not a weapon
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def use_item(item):# it stores what item was used
    global player_health
    if item == "Health Potion":# checks if health potion was used
        player_health +=40
        if player_health > 100:# to make sure it doesn't go over 100 which is max hp
            player_health = 100
        print("You used a Health Potion for 40 health!")
        print(f"Your health: {player_health}")
        inventory.remove(item)  # Remove the health potion from the inventory after using it
        print(f"{item} has been removed from your inventory.")
    else:
        print("Item not recognized.")


def see_inventory():# this function tells the user what they have
    print("\nYour inventory:")
    print(f"\nYour current gold: {gold}")  # reminds them how much gold they have

    if inventory:
        for item in inventory:
            print(f"- {item}") # makes everything in lines so it's easier to read
    else:
        print("Your inventory is empty.")

    print(f"\nCurrently equipped weapon: {equipped_weapon} (Damage: {weapons[equipped_weapon]})")# prints the weapon they are using and the damage


def rules(): # basic rules the only prints at the start of the game
        print("Welcome to my game!")
        print("Mr Hutt has turned everyone evil with his mind control device.")
        print("Defeat Mr Hutt and destroy his mind control device to save the school.")
        print("You start with a shovel as your weapon.")
        print("You can buy items from the in-game shop.")
        print("You start with 15 gold and can earn more by fighting.")
        print("For every mob you deafeat you gain 10 gold")
        print("Have fun!")
        first_option()


def rules2():# basic print code
    print("\n--- Survival Game ---")
    print("1. Continue with the game")
    print("2. Enter the shop")
    print("3. Check your inventory")
    print("4. Equip weapon/use item")
    print("5. Quit")


def first_option():
    global gold

    while True:
        rules2()  # prints rules2 and then goes back to the code
        command = input("> ").strip()  # gets an answer from the player and removes spaces in userinput answer just incase

        if command == "1":
            story()  # Go to the story section
        elif command == "2":
            shop()
        elif command == "3":
            see_inventory()
        elif command == "4":
            equip_weapon()
        elif command == "5":
            print("Thanks for playing!")
            quit()
        else:
            print("\nInvalid command. Try again.")
def apply_extra_damage(damage):# this functinon is used is the user has a hammer because hammer has a special abillity that does extra damage

    if equipped_weapon == "Hammer":
        if random.random() < 0.25:  # 25% chance to apply extra damage
            extra_damage = damage * 0.25  # 25% of the base damage
            damage += extra_damage  # Add extra damage to the total damage
            print(f"Your hammer does extra damage! ({extra_damage} added)")
    return damage

def attack(enemy):# this function attacks the mob
    damage = weapons[equipped_weapon] # creating a varible to use
    damage = apply_extra_damage(damage)
    enemy["health"] -= damage  # Apply the damage
    if enemy["health"] < 0:
        enemy["health"] = 0  # Clamp health to zero
    print(f"\nYou attack the {enemy['name']} with your {equipped_weapon} for {damage} damage!")

    if enemy["health"] == 0:
        print()# no need to print anything because my other function does it
    else:
        print(f"The {enemy['name']} now has {enemy['health']} health left.")

def zombie_attack(player_health, enemy):# this function makes the mob attack you
    damage = enemy["damage"]  # Get the zombie's attack damage
    weapon = enemy["weapon"]  # Get the weapon used by the enemy
    player_health -= damage  # Subtract the damage from the player's health
    print(f"\nThe {enemy['name']} attacks you with their {weapon} for {damage} damage!")

    if player_health <= 0:
        print()  # This part is blank because another function will tell them how much hp they have
        play_again()  # Trigger the play_again function if player is defeated
        return 0  # Return 0 if the player is defeated
    else:
        return player_health
def heavy_attack(enemy):# this function is the heavy attack function which makes you do 2x damage but 50% of missing

    miss_chance = 0.5  # 50% chance to miss
    if random.random() < miss_chance:
        print("You swing your weapon with maximum force but the enemy predicted your attack...")
        print("you missed your attack")
        return 0  # No damage if it misses
    else:
        damage = weapons[equipped_weapon] * 2  # Double damage for heavy attack
        damage = apply_extra_damage(damage)
        enemy["health"] -= damage
        print(f"You deal {damage} damage to the {enemy['name']} with your heavy attack!")
        return damage
def defense(enemy):# this function should be called deflect but if i change it i would have to change a lot
    global player_health
    original_damage = enemy["damage"]  # Zombie's original damage
    absorbed_damage = original_damage * 0.7  # Absorbed 70% of the damage
    reflected_damage = original_damage * 0.3  # Reflectes and deals 30% of the damage of zombie attack

    reflected_damage = apply_extra_damage(reflected_damage)
    player_health -= absorbed_damage # Player absorbs 70% of the damage
   
    enemy["health"] -= reflected_damage# Reflects 30% of the damage to the enemy
    print(f"You absorb {absorbed_damage:.2f} damage and reflect {reflected_damage:.2f} damage back to the {enemy['name']}!")# makes it so that its 2 decimal places
    return player_health
def handle_battle(enemy):# handles all the fights against mobs
    global player_health
    global gold
    while player_health > 0 and enemy["health"] > 0:
        print("Choose Your opition")
        print("1. Attack - attacks enemy for how much your weapon deals")
        print("2. Deflect - Obsorbs 70% of the damage and reflects 30% back, this move is good when the enemy does lots of damage")
        print("3. Heavy Attack - 50% chance of dealing twice the damage 50% chance of missing the attack")
     
        try:# incase they typo
            action = input("> ").lower()

            if action == "1":  # If the player chooses "attack"
                if synonym_game("attack") == True:  # Call the scramble game if they get it wrong they miss their attack
                    attack(enemy)  # Perform the attack action
                    if enemy["health"] <= 0:
                        print(f"You defeated the {enemy['name']}!")
                        gold += 10  # Give 10 gold upon winning
                        print(f"You received 10 gold! Your total gold is now {gold}")
                        return
                    else:
                        # If the enemy is still alive, the enemy counterattacks
                        player_health = zombie_attack(player_health, enemy)
                        print(f"Your current health: {player_health}")
                        print()
                        if player_health <= 0:
                            print()
                            return
                else:
                    player_health = zombie_attack(player_health, enemy) # Directly print the updated player health after damage
                    print(f"Your current health: {player_health}")
                    return handle_battle(enemy)  # Retry the battle                  
            elif action == "2":  # If the player chooses "defend"
                if synonym_game("defend") == True:  # Call scramble game
                    defense(enemy)  # Perform the deflect action
                    if enemy["health"] <= 0:
                        print(f"You defeated the {enemy['name']} by reflecting damage!")
                        gold += 10  # Give 10 gold upon winning
                        print(f"You received 10 gold! Your total gold is now {gold}")
                        return
                    else:
                        # If the enemy is still alive, the enemy counterattacks
                        player_health = zombie_attack(player_health, enemy)
                        print(f"Your current health: {player_health}")
                        print()
                        if player_health <= 0:
                            print()
                            return
                else:
                    player_health = zombie_attack(player_health, enemy) # Directly print the updated player health after damage
                    print(f"Your current health: {player_health}")
                    return handle_battle(enemy)  # Retry the battle                  
            elif action == "3":  # If the player chooses "heavy"
                if synonym_game("heavy attack") == True:  # Call spelling challenge for heavy attack
                    heavy_attack(enemy)  # Perform the heavy attack action
                    if enemy["health"] <= 0:
                        print(f"You defeated the {enemy['name']} with a heavy attack!")
                        gold += 10  # Give 5 gold upon winning
                        print(f"You received 10 gold! Your total gold is now {gold}")
                        return
                    else:
                        # If the enemy is still alive, the enemy counterattacks
                        player_health = zombie_attack(player_health, enemy)
                        print(f"Your current health: {player_health}")
                        print()
                        if player_health <= 0:
                            print()
                            return
                else:
                    player_health = zombie_attack(player_health, enemy) # print the updated player health after damage
                    print(f"Your current health: {player_health}")
                    return handle_battle(enemy)  # Retry the battle until they die or win
            else:
                print("Invalid action! Choose 'attack', 'defend', or 'heavy'.")
                return handle_battle(enemy)  # Prompt again if invalid input
        except ValueError:
            print("Please enter a valid input.")
def synonym_game(action_type):# this is the scramble game it takes a random word from a list and if they get it right you will attack also the word gets removed so they cant get it again

    word, synonym_list = random.choice(list(synonyms.items()))  
    print(f"\nYou must unscramble the words to {action_type}!")  
    print(f"you have 20 seconds to answer")
    print(f"Scrambled word: {word}")  # Display the scrambled word
    print(f"Clue: {synonym_list[1]}")  # Provide a clue to help the player

    max_time = 20  # Set the maximum time allowed
    start_time = time.time()  # Start the timer
    guess = input("Enter your guess: ")  # Player enters their guess
    elapsed_time = time.time() - start_time  # Measure elapsed time

    if elapsed_time > max_time:  # Check if time has exceeded the max_time
        print("\nTime's up! You lose your turn.")
        return False  # Timeout

    if guess.lower() in synonym_list[0]:  # Check if the player's guess is correct
        print(f"\nCorrect! You successfully performed {action_type}!")  # Correct guess message
        del synonyms[word]  # Remove the word from the synonyms dictionary after it is guessed correctly
        return True  # Correct guess
    else:
        print("\nIncorrect! You lose your turn.")
        return False  # Incorrect guess
def story():# from this point onwards all the code is very repeatitive the story is pretty long
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
    zombie_weights = [1, 0, 0, 0, 0, 0, 0, 0]# the chance of encountering a mob 100% of encounter evil corridor
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"You climb up the stairs of the towerblock a {enemy['name']} attacks!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # so after winning a fight and going to the next function it will go to rules2 which is the menu this is so the user can quit whenever they feel like it
        #also so if they want to buy a weapon to prepare for next round they can do so
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. Explore first floor")
                    print("2. Go up to the second floor")                  
                    while True:  # This loop keeps asking until a valid option is selected
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                explore_first()  # goes to a part of the story
                                break  # exits if input error
                            elif next_choice == 2:
                                second()  # goes to a part of the story
                                break  # exits if input error
                            else:
                                print("Invalid choice. Please choose 1 or 2.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def explore_first():
    zombie_weights = [0, 1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"As you make it up to the first floor a {enemy['name']}")
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

                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                explore_halls()
                                break
                            elif next_choice== 2:
                                explore_bridge()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()                  
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
               
def explore_halls():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"You walk around the halls slowly and silently and then {enemy['name']} appares!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore elevator YOU MUST NEED LIFT PASS")
                    print("2. explore classes")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                explore_elevator()
                                break
                            elif next_choice== 2:
                                explore_class()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def explore_bridge():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"As you make it to the school bridge a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. explore 'STAFF ONLY' room there is a note that says STAFF ONLY")
                    print("2. explore under the bridge")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                explore_staff()
                                break
                            elif next_choice== 2:
                                explore_downstairs()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def explore_staff():
    print("You dont listen to the staff only note and go in anyway a bunch of teachers start coming towards you, you are outnumbered")
    print("You lose")
    play_again()
def explore_downstairs():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
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
                    break

                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def explore_elevator():
    print("You go into the elevator even though it says you must have a lift pass")
    print("there are 5 teachers in the elevator who start coming towards you")
    print("you lose")
    play_again()
def explore_class():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You walk into a class full of computers suddenly in the corner of your eye you see{enemy['name']} ")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("You walk into a class")
                    FINAL_PART()
                    break
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def second():
    zombie_weights = [0, 1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"As you climb up to the second floor of the tower block, you encounter a {enemy['name']}!")
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
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                explore_second()
                                break
                            elif next_choice== 2:
                                explore_third()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
               
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")

def explore_second():
    # Define zombie weights for random choice
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the second floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)
    # Check if player is still alive after the battle
    if player_health > 0:
        rules2()  # Show rules2 after battle
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("What would you like to do next?")
                    print("1. Go talk to the student")
                    print("2. Go up the elevator - YOU MUST HAVE A LIFT PASS")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                student()  
                                break
                            elif next_choice == 2:
                                explore_elevator()  
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                         
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def student():
    if player_health > 0:
            print("The student tells you what you need to do to save wc is to go to the libary and thats where the mind control device is")
            print("Do you trust the student - he looks kind of guilty")
            while True:
                print("1. go to the libary")
                print("2. go explore the third floor")
                try:
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        libary()
                        break
                    elif next_choice == 2:
                        print("you dont listen to him")
                        print("and go to the third floor")
                        explore_third()
                        break           
                    else:
                        print("Invalid choice. Returning to previous options.")
                except ValueError:
                    print("Please enter a valid number")
def libary():
    print("you were betrayed")
    print("You dont trust your instincts instead trusting the little student")
    print("He leads you to the teachers meeting and you get teamuped against the zombies")
    play_again()
def explore_third():
    # Define zombie weights for random choice
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats2, weights=zombie_weights, k=1)[0]
    print(f"As you climb up the third floor of the tower block, you encounter a {enemy['name']}!")

    # Call battle logic
    handle_battle(enemy)
   
    # Check if player is still alive
    if player_health > 0:
        rules2()  # Show rules after battle
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Explore the tools room.")
                    print("2. Go up the elevator YOU MUST NEED LIFT PASS")
                    next_choice = int(input("> "))
                    if next_choice == 1:
                        explore_tools()  # Placeholder for tools room exploration
                        break
                    elif next_choice == 2:
                        explore_elevator()  # Placeholder for elevator exploration
                        break
                    else:
                        print("Invalid choice. Returning to previous options.")
           
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def explore_tools():
    # Define zombie weights for random choice
    zombie_weights = [0, 0, 0, 1, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you dig around the dusty room you encounter a {enemy['name']}!")
    handle_battle(enemy)

    if player_health > 0:
        rules2()  # Show rules after battle
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("You found a key")
                    print("1. Go to the mysterious room.")
                    print("2. Go up to the fourth floor.")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                mystery_room()  # Placeholder for mysterious room logic
                                break
                            elif next_choice == 2:
                                fourth_floor()  # Placeholder for fourth floor logic
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
               
                        except ValueError:
                            print("Please enter a valid number.")  # Handle invalid input
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def mystery_room():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
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
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def fourth_floor():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you climb up to the fourth floor of the tower block, you encounter a {enemy['name']}!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Use your key to go inside the loud room")
                    print("2. Go up on top of the tower block")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                loud()
                                break
                            elif next_choice == 2:
                                top_floor()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                 
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def top_floor():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
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
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def loud():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"Mr hunt is hammering his mind control device trying to improve it")
    print(f"{enemy['name']} starts coming towards you")

    handle_battle(enemy)
    if player_health > 0:
        FINAL_PART()
def road_explore():
    zombie_weights = [1, 0, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you walk along the road you encounter {enemy['name']}!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Continue on the road path")
                    print("2. Try to leave school through where the buses leave")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                continue_road()
                                break
                            elif next_choice == 2:
                                bus_path()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")

def bus_path():
    zombie_weights = [0, 0, 0, 0, 1, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You You try to leave but{enemy['name']} catches you trying!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("You see a teacher guarding the exit")
                    print("1. Go anyway")
                    print("2. Leave")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                gate()
                                break
                            elif next_choice == 2:
                                go_back()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def go_back():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You try to go back but {enemy['name']} starts questioning you")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Go into a class")
                    print("2. sports center")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                go_into_class()
                                break
                            elif next_choice == 2:
                                sport()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def sport():# this function is a little math game to play a sport
    questions_right = 0
    print("Elvis: Lets play some badminton I need some practice")
    print("how to play: answer 3 math questions to win")
    while questions_right < 3:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        symbol = random.choice(["+","-","*"])
        if symbol == "+":
            correct = num1 + num2
        elif symbol == "-":
            correct = num1 - num2
        else:
            correct = num1 * num2
        print(f"Rally {questions_right + 1}: what is {num1} {symbol} {num2}?")
        try:
            player_answer = int(input("> "))
            if player_answer == correct:
                questions_right += 1
            else:
                print("incorrect try again")
        except ValueError:
                print("please enter a number")
    print("you won the game")
    print("Mr hunt: Hey I saw you playing badminton over there now that your all tired, this is the perfect chance to defeat you")
    bus_fight()
               
def go_into_class():
    zombie_weights = [0, 0, 0, 0, 0, 1, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You walk into class and destract{enemy['name']} and his lesson!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Continue")

                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                bus_fight()
                                break

                            else:
                                print("Invalid choice.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")

def gate():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You go even though a teacher is guarding the gate you must fight {enemy['name']}")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("A bus a charging at you it looks like your only chance is to jump on to avoid getting hit")
                    print("1. try to jump on")
                    print("2. Attempt to dodge")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                into_bus()
                                break
                            elif next_choice == 2:
                                bus_dodge()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def into_bus():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You jumped into the bus {enemy['name']} is looking at you funny, he doesn't like you")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("the boss sitting at the back")
                    print("1. fight")
                    print("2. run")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                bus_fight()
                                break
                            elif next_choice == 2:
                                print("you try to run but he catches you and gets a clean hit")
                                bus_fight()
                                break
                            else:
                                print("Invalid choice. Returning to previous options.")
                   
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")

def bus_dodge():
    global player_health
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You try to dodge the bus but it hits you and you see {enemy['name']} looking down on you)")
    print(f" Boss: I knew it would work.. oh")
    print(f" you lost 25 HP")
    player_health-=25
    print(f"You now have {player_health} HP left.")
    if player_health <= 0:
            print("You collapse from the hit. Everything fades to black... you lose")
            play_again()

    print(f" you get back up to fight him")
    handle_battle(enemy)
    if player_health > 0:
        FINAL_PART()
def bus_fight():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f" you encounter {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        FINAL_PART()

def continue_road():
    zombie_weights = [0, 1, 0, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You walk around on the road then you encounter {enemy['name']}!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Canteen")
                    print("2. Finance office")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                canteen()
                                break
                            elif next_choice == 2:
                                office()
                                break
                            else:
                                print("Invalid choice.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def office():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You go inside the finacne office and you encounter {enemy['name']}!")
    handle_battle(enemy)
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    print("What would you like to do next?")
                    print("1. Go up the tower block")
                    print("2. Up the elevator YOU MUST NEED LIFT PASS")
                    while True:
                        try:
                            next_choice = int(input("> "))
                            if next_choice == 1:
                                tower_block()
                                break
                            elif next_choice == 2:
                                explore_elevator()
                                break
                            else:
                                print("Invalid choice.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def canteen():
    zombie_weights = [0, 0, 1, 0, 0, 0, 0, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"As you enter the canteen, you encounter a {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
   
    if player_health > 0:
        rules2()  # Call to show rules2 options
       
        while True:
            try:
                command = int(input("> "))
               
                if command == 1:
                    # Next step after defeating the enemy
                    print("What would you like to do next?")
                    print("1. disrespect them and eat their food")
                    print("2. Restore the canteen")
                   
                    while True:
                        try:
                            next_choice = int(input("> "))
                           
                            if next_choice == 1:
                                posion()  # Proceed to the lose part
                                break  # Break the inner loop and return to the main options
                            elif next_choice == 2:
                                restore_canteen()  # Restore the canteen
                                break  # Break the inner loop and return to the main options
                            else:
                                print("Invalid choice. Please choose again.")
                        except ValueError:
                            print("Please enter a valid number.")

                elif command == 2:
                    shop()  # Call the shop function
                    rules2()  # Exit the loop after visiting shop                
                elif command == 3:
                    see_inventory()  # Show inventory
                    rules2()  # Exit the loop after checking inventory                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()  # Exit the loop after equipping weapon                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit the game
               
                else:
                    print("Invalid choice. Please choose again.")
           
            except ValueError:
                print("Please enter a valid number.")

def posion():
    print("you try to be funny but you we're outplayed")
    print("the food that you ate was posioned")
    play_again()
               

def restore_canteen():
    print("You help them restore the canteen. They thank you by giving you a health potion.")
    inventory.append("Health Potion")
    print("You recived a Health Potion")
    print("They put you in charge of the canteen.")
    # Check if player is still alive (health > 0)
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Next step after restoring the canteen
                    print("What would you like to do next?")
                    print("1. Lay a trap")
                    print("2. Move to the maths block")                  
                    while True:
                        try:
                            next_choice = int(input("> "))
                           
                            if next_choice == 1:
                                trap()  # Lay a trap
                                break  # Break the inner loop and return to the main options
                            elif next_choice == 2:
                                maths_block()  # Move to the maths block
                                break  # Break the inner loop and return to the main options
                            else:
                                print("Invalid choice. Please choose again.")
                        except ValueError:
                            print("Please enter a valid number.")              
                elif command == 2:
                    shop()  # Visit the shop
                    rules2()  # Show rules again after the shop visit               
                elif command == 3:
                    see_inventory()  # See the player's inventory
                    rules2()  # Show rules again after inventory              
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()  # Show rules again after equipping weapon               
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit the game               
                else:
                    print("Invalid choice. Please choose again.")                   
            except ValueError:
                print("Please enter a valid number.")
def trap():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"{enemy['name']} has fallen for the trap he has lost 20HP!")
    enemy['health'] -= 20
    print(f"The {enemy['name']} now has {enemy['health']} health left")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    FINAL_PART()
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()                
                elif command == 3:
                    see_inventory()
                    rules2()                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")                    
            except ValueError:
                print("Please enter a valid number.")
def maths_block():
    if player_health > 0:
        print("Ugh, why is maths so hard?")
        print("Hey you, you look really smart...")

        while True:
            try:
                print("What would you like to do next?")
                print("1. Help Elvis with his homework")
                print("2. Ask Elvis where to go")
                command = int(input("> "))
               
                if command == 1:
                    yes()  # Call the yes function
                    break  # Exit the loop after making a choice
                elif command == 2:
                    no()  # Call the no function
                    break  # Exit the loop after making a choice
                else:
                    print("Invalid choice. Please choose again.")
           
            except ValueError:
                print("Please enter a valid number.")
def yes():
    global player_health
    print("Thanks for the help")
    print("Elvis leads you the way")

    if player_health > 0:
        rules2()  # Call to show rules2 options

        while True:
            try:
                command = int(input("> "))

                if command == 1:
                    # Next step after defeating the enemy
                    print("You see the boss right in the corner")
                    print("1. Run")
                    print("2. Fight")
                   
                    while True:
                        try:
                            next_choice = int(input("> "))
                           
                            if next_choice == 1:
                                print("You try to run but Mr. Hunt catches you as you try to flee -20HP")
                                player_health -= 20
                                print(player_health)
                                yes2()  
                                break  
                            elif next_choice == 2:
                                yes2() 
                                break  
                            else:
                                print("Invalid choice. Please choose again.")
                        except ValueError:
                            print("Please enter a valid number.")
                elif command == 2:
                    shop()  # Call the shop function
                    rules2()  # Show rules2 again                
                elif command == 3:
                    see_inventory()  # View inventory
                    rules2()  # Show rules2 again                
                elif command == 4:
                    equip_weapon()  # Equip a weapon
                    rules2()  # Show rules2 again                
                elif command == 5:
                    print("Thanks for playing!")
                    quit()  # Exit game                
                else:
                    print("Invalid choice. Please choose again.")
            except ValueError:
                print("Please enter a valid number.")                  
def yes2():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You encounter {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        FINAL_PART()
def no():
    zombie_weights = [0, 0, 0, 0, 0, 0, 1, 0]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"Elvis gets mad")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        rules2()  # Call to show rules2 options
        while True:
            try:
                command = int(input("> "))
                if command == 1:
                    # Continue the game
                    print("You search his pockets and found a map of the bosses location")
                    no2()
            except ValueError:
                print("Please enter a valid number.")
def no2():
    zombie_weights = [0, 0, 0, 0, 0, 0, 0, 1]
    enemy = random.choices(zombie_stats, weights=zombie_weights, k=1)[0]
    print(f"You encounter {enemy['name']}!")
    handle_battle(enemy)  # Battle logic moved here
    if player_health > 0:
        FINAL_PART()

def play_again():
    print("You have been defeated..")
    print("Thanks for playing")




def FINAL_PART():# this part of the game is after defeating the boss you have to defuse a mind controlling device to do so you do a puzzle
    print("you defeated the boss, mr hunt to defuse the mind controlling device you must solve a puzzle")
    # List of 5 puzzles with missing letters and hints
    puzzles = [
        {"clue": "Ki_ _", "answer": "kiwi", "hint": "It's a type of bird"},
        {"clue": "_ _ _ _ _ce", "answer": "science", "hint": "A subject"},
        {"clue": "_ _ _n", "answer": "moon", "hint": "Something large found in the sky."},
        {"clue": "_r_ _on    _r_ _t", "answer": "dragon fruit", "hint": "A fruit commonly in asia."},
        {"clue": "o _ _ _ _ _ _n", "answer": "obsidian", "hint": "Volcano"}
    ]
   
    for level in range(1, 6):  # Loop through levels 1 to 5
        # Set the time limit for each level
        if level == 1:
            max_time = 25  # Level 1 = 25 seconds
        elif level == 2:
            max_time = 25  # Level 2 = 25 seconds
        elif level == 3:
            max_time = 20  # Level 3 = 20 seconds
        elif level == 4:
            max_time = 15  # Level 4 = 15 seconds
        elif level == 5:
            max_time = 15  # Level 5 = 15 seconds
       
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
rules()# starts the game
