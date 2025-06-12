# hangman hero game

print("Welcome to the hangman hero game! GREETINGS\n")
print("In this game you need to guess the word before your lives run out - you have 6 lives only by the way or it's hell\n")
print("SO ALL THE BEST SOLDIER!\n")

lives_left = 6
wrong_guesses = []
word = ["_", "_", "_", "_"]

while True:
    letter_entered = input("Guess a letter in this 4-letter word:\n").lower()

    if letter_entered == "c":
        print(f"Yes, {letter_entered} is in the word\n")
        word[0] = "c"

    elif letter_entered == "u":
        print(f"Yes, {letter_entered} is in the word\n")
        word[1] = "u"

    elif letter_entered == "t":
        print(f"Yes, {letter_entered} is in the word\n")
        word[2] = "t"

    elif letter_entered == "e":
        print(f"Yes, {letter_entered} is in the word\n")
        word[3] = "e"

    else:
        print(f"Nope! {letter_entered} is not in the word\n")
        lives_left -= 1
        wrong_guesses.append(letter_entered)
        print("Wrong guesses so far:", wrong_guesses)

    if lives_left == 0:
        print("You have no lives left! You are dead soldier!\n")
        print("Game Over!")
        break
    elif lives_left == 1:
        print("You have 1 life left! Be careful!\n")
    else:
        print("Word: " + " ".join(word))
        print(f"You have {lives_left} lives left! Keep going!\n")

    if "_" not in word:
        print("🎉 You win! the word was cute!\n")
        print("you are the hero we needed not the one we deserved\n")
        print("Thanks for playing hangman hero! stay cute and keep coding!\n")
        break