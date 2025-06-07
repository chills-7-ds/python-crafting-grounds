# Bank simulator.py

storage_for_account = {}

def negative_check(amount):
    return amount < 0

def create_account():
    account_number = int(input("Enter a new account number: "))
    initial_deposit = float(input("Enter the initial deposit amount: "))
    name = input("Enter the account holder's name: ")

    if name == "":
        print("Name cannot be empty. Please try again.")
        return

    if account_number in storage_for_account:
        print("Account number already exists. Please try again.")
        return

    if negative_check(initial_deposit):
        print("Initial deposit cannot be negative. Please try again.")
        return

    storage_for_account[account_number] = {"name": name, "balance": initial_deposit}
    print(f"Account created successfully for {name} with ₹{initial_deposit:.2f}")

def deposit_money():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in storage_for_account:
            print("Account does not exist.")
            return

        deposit_amount = float(input("Enter amount to deposit: "))
        if negative_check(deposit_amount):
            print("Deposit amount cannot be negative.")
            return

        storage_for_account[account_number]["balance"] += deposit_amount
        print(f"Deposited ₹{deposit_amount:.2f} successfully.")
    except Exception as e:
        print("Error:", e)

def withdraw_money():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in storage_for_account:
            print("Account does not exist.")
            return

        withdraw_amount = float(input("Enter amount to withdraw: "))
        if negative_check(withdraw_amount):
            print("Withdrawal amount cannot be negative.")
            return

        if storage_for_account[account_number]["balance"] >= withdraw_amount:
            storage_for_account[account_number]["balance"] -= withdraw_amount
            print(f"Withdrew ₹{withdraw_amount:.2f} successfully.")
        else:
            print("Insufficient funds.")
    except Exception as e:
        print("Error:", e)

def check_balance():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in storage_for_account:
            print("Account does not exist.")
            return

        balance = storage_for_account[account_number]["balance"]
        name = storage_for_account[account_number]["name"]
        print(f"{name}'s balance is ₹{balance:.2f}")
    except Exception as e:
        print("Error:", e)

def menu():
    print("\n=== Welcome to the Bank Simulator ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    try:
        choice = int(input("Please select an option (1-5): "))
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            print("Thank you for using the Bank Simulator. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
    except ValueError as e:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Unexpected error:", e)

# Infinite loop to keep menu running
while True:
    menu()