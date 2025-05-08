Palindrome Checker

So this is one of those clich� projects every programmer (hopefully) has done � and this is my take on it.

This script checks whether the text you enter is a palindrome or not. A palindrome is a word, number, or sentence that reads the same forward and backward � for example: madam, racecar, palap, etc.

In my code, I started by taking input from the user (it can be text or numbers, so I didnt restrict it to just strings). Then, I wrote a simple line to clean the input � this removes any spaces or punctuation and makes the text lowercase. That way, the check is case-insensitive and works even for phrases. 

I used a one-liner for that, 
cleaned = ''.join(char.lower() for char in A if char.isalnum())

Then I used a basic if-else block to check if the cleaned string is equal to its reverse. Thats the core of the project.

Now I wanted to add two final classy additions that is, a loop so the user can keep checking words until they type quit and a comparison output showing both the cleaned input and its reversed version, so the user can clearly see how the check is done.

So I kept the main logic inside a while loop and added a condition to break when the user types quit. I also used formatted print statements (f-strings) to show both versions of the text.

No libraries were needed here. 

It used these basic Python concepts - input() and print(), for and while loops, string methods and slicing, conditionals.

Not many challenges were faced because it mostly used simple, foundational Python � how do you run it? open VS code go to terminal after you saved the entire code, just run this command - 'python palindrome_checker.py'

See you in the next one.
