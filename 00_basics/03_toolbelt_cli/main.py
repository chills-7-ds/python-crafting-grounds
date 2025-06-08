from calci import calculator
from converter import unit_converter
from password_gen import password_generator
from utils.cli_helpers import wait_for_enter


def display_menu():
    print("\nWelcome to Toolbelt CLI 🛠️")
    print("Choose a tool:")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Password Generator")
    print("4. Exit")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            print("Launching Calculator...\n")
            calculator()

        elif choice == "2":
            print("Launching Unit Converter...\n")
            unit_converter()

        elif choice == "3":
            print("Launching Password Generator...\n")
            password_generator()

        elif choice == "4":
            print("Exiting Toolbelt CLI. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")
            wait_for_enter()


if __name__ == "__main__":
    main()
# This is the main entry point for the Toolbelt CLI application.