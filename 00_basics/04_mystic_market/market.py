# Core Market Logic

player_gold = 100
player_inventory = {
    "Healing Potion": 2,
    "Mana Elixir": 1
}

shop_inventory = {
    "Healing Potion": 10,
    "Mana Elixir": 15,
    "Invisibility Draught": 25
}

def view_inventory():
    print("🧺 Your Inventory:")
    if not player_inventory:
        print(" - Empty")
    else:
        for item, qty in player_inventory.items():
            print(f" - {item} x{qty}")

def view_gold():
    print(f"💰 Gold Balance: {player_gold}")

def buy_potion():
    global player_gold
    print("Which potion would you like to buy?")
    for item, price in shop_inventory.items():
        print(f"- {item} ({price} gold)")

    choice = input("> ").strip()
    price = shop_inventory.get(choice)

    if price is None:
        print("❌ That potion doesn't exist.")
        return

    if player_gold >= price:
        player_gold -= price
        player_inventory[choice] = player_inventory.get(choice, 0) + 1
        print(f"✅ You bought a {choice}!")
    else:
        print("❌ Not enough gold!")

def sell_potion():
    global player_gold
    print("Which potion would you like to sell?")
    choice = input("> ").strip()

    if choice not in player_inventory or player_inventory[choice] == 0:
        print("❌ You don't have that potion.")
        return

    sell_price = shop_inventory.get(choice, 5) - 5  # Basic fallback price logic
    player_inventory[choice] -= 1
    player_gold += sell_price
    print(f"✅ You sold {choice} for {sell_price} gold!")

    if player_inventory[choice] == 0:
        del player_inventory[choice]

def handle_invalid_choice():
    print("❌ Invalid option. Try again.")
