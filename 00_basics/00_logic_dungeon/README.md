# 🧠 Logic Dungeon: The Lift of Logic

You're trapped on the 10th floor of a mysterious building. Only one room holds the working emergency lift. But to access it, you must answer 7 riddles.

Each riddle's answer gives one letter. Combine the first letters of the 7 answers to unlock the lift.

**Get 3 wrong? Game over.**

You're setting a global counter wrong_attempts and setting the max limit to 3. This means across all puzzles combined, the player can only mess up 3 times.

Each riddle is passed into check_answer() one after the other.

You can only go to the next riddle if the current one was solved (because it waits inside the while loop).

If the player hits 3 wrong answers anywhere along the way, the game ends instantly.

## Concepts Practiced
- Variables
- Loops
- Conditionals
- Functions

No libraries were used.

## Advice
be careful on the indentation y'all 

## How to Run
```bash
python main.py
```

see you in the next one!