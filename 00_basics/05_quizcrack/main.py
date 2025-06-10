from quizzes import get_questions  

def game():
    while True:  # Keeps the game running until the user chooses to exit
        print("🎮 Welcome to QuizCrack! Test your wits 🧠\n")

        name = input("Enter your name: ")
        print(f"\nHi {name}! Choose a category:")
        
        categories = {
            "1": "Science",
            "2": "History",
            "3": "Pop Culture"
        }
        print("select from the following categories:")
        for key, value in categories.items():
            print(f"{key}. {value}")


        category_choice = input("Select a category (1-3): ")

        questions = get_questions(category_choice)  

        if questions is None:
            print("Invalid choice. Exiting the game.")
            exit()

        score = 0

        for i, q in enumerate(questions, 1):
            print(f"🔬 Question {i}: {q['question']}")
            for option in q['options']:
                print(option)
            
            answer = input("> ").strip().lower()
            
            if answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

        print(f"🎯 You scored {score} out of {len(questions)}!")

        percentage = (score / len(questions)) * 100

        print(f"\n🎉 You got {score} out of {len(questions)} right, {name}!")
        print(f"🏆 Your Score: {percentage:.0f}%")

        if percentage == 100:
            print("💡 Bonus Fact: Mars has the tallest volcano in the solar system!")

        play_again = input("\nWanna play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing QuizCrack!")
            break  # Exits the loop instead of using recursion

# Start the game
game()