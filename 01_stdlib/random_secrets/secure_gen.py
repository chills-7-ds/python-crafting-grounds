# secure_generator.py
import random
import secrets
import string

def generate_password(length=12):
    """Generate a secure password using secrets."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_code():
    """Generate a simple 6-digit random verification code."""
    code = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return code

def main():
    print("🔐 Secure Generator CLI")
    print("------------------------")
    print("1. Generate Secure Password")
    print("2. Generate Random 6-digit Code")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        length = int(input("Enter password length: "))
        print(f"\nYour Secure Password: {generate_password(length)}")
    elif choice == "2":
        print(f"\nYour Verification Code: {generate_code()}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
