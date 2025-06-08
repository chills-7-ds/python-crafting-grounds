# converter.py

def unit_converter():
    print("\n-- Unit Converter --")
    try:
        print("Choose conversion type:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            km = float(input("Enter distance in kilometers: "))
            miles = km * 0.621
            print(f"{km} km is {miles} miles.")

        elif choice == "2":
            miles = float(input("Enter distance in miles: "))
            km = miles / 0.621
            print(f"{miles} miles is {km} kilometers.")

        else:
            print("Invalid choice.")

    except Exception as e:
        print("Error:", e)

    input("Press Enter to return...")
