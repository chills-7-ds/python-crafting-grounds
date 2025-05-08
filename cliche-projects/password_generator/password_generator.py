import string
import random

while True:
    try:
        password_length = int(input("Enter the length of the password: \n"))
        if password_length < 8:
            print("⚠️  Password must be at least 8 characters.")
            retry = input("Do you want to enter a new length? (y/n): ").strip().lower()
            if retry != 'y':
                print("Exiting password generator.")
                exit()
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


if password_length < 8:
    print("Password length must be at least 8 characters. Please try again.")
else:
    char_pool = string.ascii_letters + string.digits + string.punctuation

    while True:
        generated_password = random.choices(char_pool, k=password_length)
        x = "".join(generated_password)

        has_digit = any(char.isdigit() for char in x)
        has_lower = any(char.islower() for char in x)
        has_upper = any(char.isupper() for char in x)
        has_symbol = any(char in string.punctuation for char in x)

        if has_digit and has_lower and has_upper and has_symbol:
            break  

    print("Generated password:\n", x)

    def check_password_strength(password):
        if len(password) < 8:
            return "Weak: Password must be at least 8 characters long.\n"
        if not any(char.isdigit() for char in password):
            return "Weak: Password must contain at least one digit.\n"
        if not any(char.islower() for char in password):
            return "Weak: Password must contain at least one lowercase letter.\n"
        if not any(char.isupper() for char in password):
            return "Weak: Password must contain at least one uppercase letter.\n"
        if not any(char in string.punctuation for char in password):
            return "Weak: Password must contain at least one special character.\n"

        if len(password) < 12:    
            strength = "Moderate\n"
        else:
            strength = "Strong\n"

        return strength 

    print("Password strength:\n", check_password_strength(x)) 