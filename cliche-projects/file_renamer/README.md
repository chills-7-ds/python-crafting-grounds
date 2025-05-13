File renamer

So this is that classic project every beginner probably does at some point and this is my take on it.

First off, a file renamer lets you rename all the files in a given folder according to a defined pattern (i.e, if you want to make it all lowercase or replace parts of the file name etc). 

In python, os is a standard library module that allows you to interact with the operating system. The moment you import os you gain access to functions that let your python work with things like,
-> files & directories (ex: os.getcwd(), os.chdir, os.listdir(path = "."))
-> paths (ex: os.path.join(path1,path2),os.path.exists(path))
-> env variables (ex: os.environ, os.getenv('VAR'))
-> process and management (ex: os.system('commmand'), os.name)

The Backend,
1. The script uses the `os` module to:
   - List all files in the specified folder.
   - Check if a file has already been renamed.(so you'll not get an output saying 'renamed_renamed_testfile1.txt')
   - Rename files using the `os.rename()` function.
2. The script ensures that only files (not directories) are renamed.
3. The renamed files are prefixed with `renamed_`.

The core program or code is over.

if you want to add some additions go for adding underscores, taking prompts from the user for a pattern of their choice, adding undo support, CLI arguements and timestamps. i will add these features later in advanced_file_renamer folder - wait a bit!

1 library were needed here - the os module.

It used these basic Python concepts - input() and print(), for and while loops, string methods and slicing, conditionals.

Not many challenges were faced because it mostly used simple, foundational Python � how do you run it? open VS code go to terminal after you saved the entire code, just run this command - 'python palindrome_checker.py'

See you in the next one.