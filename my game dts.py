import random


gold = 30
zombie_stats = [{"name": "evil corridor defender", "health": 30,"weapon": "hands","damage": random.randint(1,3)}, # these are all the mobs and their characistics
                {"name": "evil senior student", "health": 50,"weapon": "stick","damage": random.randint(3,5)},
                {"name": "evil teacher", "health": 30,"weapon": "hands","damage": random.randint(5,10)},
                {"name": "miniboss", "health": 30,"weapon": "hands","damage": random.randint(7,15)}]

Your_ally = [{"name": "user", "health": 100,"weapon": "shovel","damage": 12}] # the users characistics
inventory = [] # the inventory that uesr will carry



def shop():
    global gold


    items = {
        "Health potion": 20,
        "Sword": 35
        }# what can be bought 
    
    while True:
        print("\n--- Shop ---")
        print(f"your gold: {gold}")
        print("1. Buy Sword 35 gold")
        print("2. Buy Health Potion 20 gold")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if gold >= 35:
                inventory.append("sword")  # Directly add the item to inventory
                gold -= 35
                print("Sword added to your inventory.")
            else:
                print("you cant afford this item")
        
        elif choice == "2":
            if gold >= 20:
                inventory.append("Health Potion")  # Directly add the item to inventory
                gold -= 20
                print("Health Potion added to your inventory.")
            else:
                print("you cant afford this item")
                
        
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
        if command == "1":
            story() # start the story
        elif command == "2":
            shop()  # Enter the shop system
        elif command == "3":
            print(f"\nYour current gold: {gold}")
            see_inventory() # look at your items
        elif command == "4": 
            print("Thanks for playing!")
            quit() # quit the game

        else:
            print("\nInvalid command. ")


def story():
    print("your goal is to make it out through the gut buster which is near the art block")
    print("you are currently at the motorcycle parking")
    print("1. go up the tower block")
    print("2. go up the road")
    command = int(input("> "))

def story1_1():
    print("As you climb up to the first floor you find yo")


    
    



rules()


