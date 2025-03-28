import random

gold = 300
inventory = ["Shovel"]  # Start with a shovel
equipped_weapon = "Shovel"  # Start with a shovel equipped

weapons = {
    "Shovel": 12,
    "Sword": 20
}

items = {
    "Health Potion": {"type": "heal", "amount": 30},  # Heals 30 HP
    "Cure Potion": {"type": "revive", "amount": 50}   # Revives a zombie ally with 50 HP
}

zombie_stats = [
    {"name": "evil corridor defender", "health": 30, "weapon": "hands", "damage": random.randint(1, 3)},
    {"name": "evil senior student", "health": 50, "weapon": "stick", "damage": random.randint(3, 5)},
    {"name": "evil teacher", "health": 30, "weapon": "hands", "damage": random.randint(5, 10)},
    {"name": "miniboss", "health": 30, "weapon": "hands", "damage": random.randint(7, 15)}
]

your_ally = [{"name": "user", "health": 100, "attack": {"Shovel": 12}}]


def shop():
    global gold

    items = {"Health Potion": 20,
             "Sword": 35,
             "cure potion": 45}

    while True:
        print("\n--- Shop ---")
        print(f"Your gold: {gold}")
        print("1. Buy Sword (35 gold)")
        print("2. Buy Health Potion (20 gold)")
        print("3. Buy Cure Potion (50 gold)")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if gold >= 35:
                inventory.append("Sword")
                gold -= 35
                print("Sword added to your inventory.")
            else:
                print("You can't afford this")
            break

        elif choice == "2":
            if gold >= 20:
                inventory.append("Health Potion")
                gold -= 20
                print("Health Potion added to your inventory.")
            else:
                print("You can't afford this")
            break

        elif choice == "3":
            if gold >= 45:
                inventory.append("Cure Potion")
                gold -= 45
                print("Cure Potion added to your inventory.")
            else:
                print("You can't afford this")
            break

        if choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

def equip_weapon():

    global equipped_weapon

    weapons_in_inventory = [item for item in inventory if item in weapons]
    items_in_inventory = [item for item in inventory if item in items]

    # Display weapons and items
    print("\nYour weapons and items:")
    
    # Display weapons
    for i in range(len(weapons_in_inventory)):
        print(f"{i + 1}. Equip {weapons_in_inventory[i]} (Damage: {weapons[weapons_in_inventory[i]]})")
    
    # Display items
    for i in range(len(items_in_inventory)):
        print(f"{i + 1 + len(weapons_in_inventory)}. Use {items_in_inventory[i]}")

    try:
        choice = int(input("Choose a weapon/item: "))
        
        # Equip weapon
        if 1 <= choice <= len(weapons_in_inventory):
            equipped_weapon = weapons_in_inventory[choice - 1]
            print(f"You equipped the {equipped_weapon}!")

        # Use item
        elif len(weapons_in_inventory) < choice <= len(weapons_in_inventory) + len(items_in_inventory):
            item_choice = items_in_inventory[choice - len(weapons_in_inventory) - 1]
            use_item(item_choice)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def use_item(item):
    if item == "Health Potion":
        print("You used a Health Potion!")
        # Add healing logic here if needed
    elif item == "Cure Potion":
        print("You used a Cure Potion!")
        # Add revive logic here if needed
    else:
        print("Item not recognized.")


def see_inventory():
    print("\nYour inventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

    print(f"\nCurrently equipped weapon: {equipped_weapon} (Damage: {weapons[equipped_weapon]})")


def attack(enemy):
    damage = weapons[equipped_weapon]
    enemy["health"] -= damage
    print(f"\nYou attack the {enemy['name']} with your {equipped_weapon} for {damage} damage!")


def rules():
    print("Welcome to my game!")
    print("Your goal is to leave the school.")
    print("You start with a shovel as your weapon.")
    print("You can buy items from the in-game shop.")
    print("You start with 30 gold and can earn more by fighting.")
    print("Your journey begins at the motorcycles, and you must escape through the gutbuster.")
    print("Fight the evil, cure them, and buy weapons to survive.")
    first_option()


def rules2():
    print("\n--- Survival Game ---")
    print("1. Continue with the game")
    print("2. Enter the shop")
    print("3. Check your inventory")
    print("4. Equip a weapon")
    print("5. Quit")


def first_option():
    global gold

    while True:
        rules2()
        command = input("> ").strip()

        if command == "1":
            story()
        elif command == "2":
            shop()
        elif command == "3":
            print(f"\nYour current gold: {gold}")
            see_inventory()
        elif command == "4":
            equip_weapon()
        elif command == "5":
            print("Thanks for playing!")
            quit()
        else:
            print("\nInvalid command. Try again.")


def story():
    while True:
        print("Your goal is to make it out through the gutbuster, near the art block.")
        print("You are currently at the motorcycle parking.")
        print("1. Go up the tower block")
        print("2. Go up the road")

        try:
            command = int(input("> "))
            if command == 1:
                story1_1()
            elif command == 2:
                print("You take the road, but dangers lie ahead...")
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number.")


def story1_1():
    enemy = random.choice(zombie_stats)
    print(f"As you climb up the first floor of the tower block, you encounter a {enemy['name']}!")

    while enemy["health"] > 0:
        print(f"\n{enemy['name']} - Health: {enemy['health']}")
        print("1. Attack")
        print("2. Run")

        try:
            command = int(input("> "))
            if command == 1:
                attack(enemy)
                if enemy["health"] <= 0:
                    print(f"You defeated the {enemy['name']}!")
                    break
            elif command == 2:
                print("You run away safely!")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a number.")


rules()
