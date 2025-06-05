from puzzles import run_puzzle
from game_logic import start_game

if __name__ == "__main__":
    start_game()
    
    success = run_puzzle()

    if success:
        print("Now, you need to enter the password to unlock the emergency lift.")
        password = input("Enter the password: ")

        if password == "cryptic":
            print("You have successfully unlocked the emergency lift!")
            print("Congratulations! You've solved the puzzle and escaped the dungeon!")
        else:
            print("You have failed to unlock the emergency lift.")
            print("You will remain in the dungeon forever. Game over!")