# 🗂️ Directory Explorer

# Overview
Directory Explorer is a beginner-friendly Python script that lets you explore the contents of any folder on your system. It lists all files and folders, shows their sizes, and gives you a quick summary — all from the terminal. It's a lightweight utility to practice file system navigation using Python's `os` module.

# Goal
The main goal is to demonstrate how to interact with the file system using Python’s built-in `os` module — including listing files, checking paths, determining file types, and calculating file sizes — without relying on any external libraries.

# Tech Stack
- **Language:** Python
- **Libraries:** `os` (built-in)
- **Database:** None

# Features
- List all files and folders in a given directory
- Separately displays files and directories
- Shows file sizes in kilobytes
- Counts and displays the number of files and folders
- Uses the current directory as default if no path is provided

# How to Run

1. Clone or download the script:
   ```bash
   git clone <your-repo-url>
   cd <your-folder>
```

2. Run the script:

   ```bash
   python explore_dir.py
   ```

3. When prompted, enter the path of the folder you want to explore. Or just press enter to explore the current directory.

# Possible Extensions

* Add recursive directory exploration (including subfolders)
* Add filtering by file extension (e.g., show only `.txt` or `.jpg`)
* Export output to a `.txt` or `.csv` report
* Use `argparse` for command-line arguments instead of input prompts
* Add color formatting to the terminal output for better readability

# Extended Project Docs on Notion
* For behind-the-scenes thought processes((hints, expected output, aha moments)), future improvements, project roadmap, and helpful resources and references, check out the dedicated Notion site:{[link_for_the_doc](https://dramatic-psychology-0d8.notion.site/os-project-23603656c6c380dd8702eb2c5f497bb8?source=copy_link)}

**See you in the next one!**