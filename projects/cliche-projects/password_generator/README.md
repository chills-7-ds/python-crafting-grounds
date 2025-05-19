password generator 

So this is that classic project every beginner probably does at some point and this is my take on it.

First off a password generator is a program that takes password length as the input and generates a password for you. 

The backend for this one is, once you give the password length (preferably above 7) it makes a character pool of all numbers, special characters, variables you can think of and it picks random characters from the character pool with the help of 'random.choices' function from 'random' library (a standard Python library used to generate random numbers and selections). Then combine these random pieces with the help of 'join' (a string method in Python) to generate the password. 

The core of the program is done until here, now it could use a few classy additions.

So i added these, 
* Regenerate passwords until all 4 character types are present (To make sure the password is actually strong, I made it include at least one of each character type, and if it didn’t, it regenerates automatically until it passes that test. )

* Print the password and its strength only once, cleanly (for the user to know whether their password is Strong or moderate)

* Ensure the password length is at least 8. (it calls you off if it is below 8)

* Ask if the user wants to try again if they enter something too short by mistake. (if it is less than 8, the program just tells you off and gives you n number of chances to try and the user can exit anytime by pressing 'n') - always an option.

This script generates a password for you —none of the weak passwords will be generated as i coded it that way so either moderate or strong.

No external libraries were needed—just the good old `random` and `string` modules from Python's standard library.

It used these basic Python concepts - input() and print(), conditionals, random.choices(), string operations, conditionals, loops (to regenerate weak passwords), basic validation.

Not many challenges were faced because it mostly used simple, foundational Python � how do you run it? open VS code go to terminal after you saved the entire code, just run this command - 'python password_generator.py'

See you in the next one.