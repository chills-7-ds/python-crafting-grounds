from market import view_inventory, view_gold, buy_potion, sell_potion, handle_invalid_choice

def show_menu():
    print("\n🔮 Welcome to the Mystic Market 🔮")
    print("What would you like to do?")
    print("1. View Inventory")
    print("2. Buy Potion")
    print("3. Sell Potion")
    print("4. View Gold Balance")
    print("5. Exit")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("> "))
            if choice == 1:
                view_inventory()
            elif choice == 2:
                buy_potion()
            elif choice == 3:
                sell_potion()
            elif choice == 4:
                view_gold()
            elif choice == 5:
                print("🧙‍♂️ Safe travels, adventurer!")
                break
            else:
                handle_invalid_choice()
        except ValueError:
            print("⚠️ Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
