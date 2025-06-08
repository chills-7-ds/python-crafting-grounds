# password_gen.py

def password_generator():
    print("\n-- Password Generator --")
    try:
        options = [
            "sunShine9!",
            "moon_Light22",
            "crystal#Key",
            "windBlow*7",
            "fire&Stone8"
        ]
        for i, pwd in enumerate(options, start=1):
            print(f"{i}. {pwd}")
        
        choice = input("Pick a number (1-5) to choose your password: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 5:
            print(f"Your generated password is: {options[int(choice) - 1]}")
        else:
            print("Invalid choice. Here's the first password by default:")
            print(options[0])

    except Exception as e:
        print(f"Error: {e}\n")

    input("Press Enter to return...")
