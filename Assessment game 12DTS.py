import random
import sys

gold = 30
zombie_stats = [{"name": "evil corridor defender", "health": 30,"weapon": "hands","damage": random.randint(1,3)}, # these are all the mobs and their characistics
                {"name": "evil senior student", "health": 50,"weapon": "stick","damage": random.randint(3,5)},
                {"name": "evil teacher", "health": 30,"weapon": "hands","damage": random.randint(5,10)},
                {"name": "miniboss", "health": 30,"weapon": "hands","damage": random.randint(7,15)}]

Your_ally = [{"name": "user", "health": 100,"weapon": "shovel","damage": 12}] # the users characistics
inventory = [] # the inventory that uesr will carry



def shop():
    print("welcome to the shop")

    items = {
        "health potion": 20,
        "sword": 35
        }# what can be bought 
    
    while True:
        print("\n--- Shop ---")
        print("1. Buy Sword (gold :35)")
        print("2. Buy Health Potion (gold :20)")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            inventory.append("sword")  # Directly add the item to inventory
            gold = gold - 35
            print("Sword added to your inventory.")
        
        elif choice == "2":
            inventory.append("Health Potion")  # Directly add the item to inventory
            print("Health Potion added to your inventory.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Try again.")

def see_inventory():
    print("\nYour items:")
    for item in inventory:  # Print all items in the inventory
        print(f"- {item}")
    else:
        # This will run if the loop doesn't break, which means the inventory is empty
        if not inventory:  # If inventory is empty
            print("Your inventory is empty.")
    

def rules():
    print("Welcome to my game")
    print("Your goal is to leave the school")
    print("you can buy stuff from the ingame shop")
    print("you will start off with 30 gold and will be able to get more as you fight")
    print("You start by the motorcycles and you have to leave through the gutbuster")
    print("Fight the evil, cure them and buy weapons to survive")
    first_opition()

def rules2():
    print("\n--- Survival Game ---")
    print("type '1' to continue with the game")
    print("Type '2' to enter the shop")
    print("Type '3' to check your inventory")
    print("type '4' to quit")

def first_opition():
    global gold
    
    while True:
        rules2()
        command = input("> ").lower()  # Get the player's command

        if command == "2":
            shop()  # Enter the shop system
        elif command == "3":
            print(f"\nYour current gold: {gold}")
            see_inventory()
        elif command == "4":
            print("Thanks for playing!")  # Quit the game
            sys.exit()

        else:
            print("\nInvalid command. ")



    



rules()

