# puzzles.py

# Global variable to track wrong attempts
wrong_attempts = 0
MAX_ATTEMPTS = 3

def run_puzzle():
    global wrong_attempts
    print("You will face a series of puzzles to escape the dungeon.")
    print("Solve them correctly to unlock the emergency lift.")
    print("❗ You only have 3 total wrong attempts. Use them wisely.\n")

    def game_over():
        print("\n💀 GAME OVER: You’ve made 3 wrong attempts. The dungeon claims you.")
        exit()

    def check_answer(prompt, correct_answer):
        global wrong_attempts
        while wrong_attempts < MAX_ATTEMPTS:
            answer = input(prompt + "\n> ").strip().lower()
            if answer == correct_answer:
                print("✅ Correct! You may proceed.\n")
                return True
            else:
                wrong_attempts += 1
                attempts_left = MAX_ATTEMPTS - wrong_attempts
                print(f"❌ Incorrect! Attempts left: {attempts_left}\n")
                if wrong_attempts >= MAX_ATTEMPTS:
                    game_over()

    # Puzzles chain
    check_answer("I have hands but no arms. I tell time every day.🕰️", "clock")
    check_answer("I show you yourself, but I’m not you. I live on the wall.🪞", "reflection")
    check_answer("I am a question that can be spoken in one letter...", "y")
    check_answer("I keep things safe. You need numbers or words to open me.🔐", "password")
    check_answer("I fall from your eyes when you're sad or happy.😭", "tears")
    check_answer("I help you dream things that aren’t real. I live in your mind.🧠", "imagination")
    check_answer("I help solve mysteries. I’m a small piece of a big puzzle.🕵️", "clue")

    print("You have solved all the puzzles! wanna unlock the emergency lift? the password is the first letters of all your answers.")
    return True