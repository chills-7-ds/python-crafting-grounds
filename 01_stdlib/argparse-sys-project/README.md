# TextWiz

## Overview

TextWiz is a simple command-line utility to transform and analyze text. It allows quick manipulations like reversing text, converting to uppercase, counting words and characters, and checking memory usage—useful for scripting, text processing, or learning CLI text handling.

## Goal

To provide a lightweight Python tool demonstrating basic text transformations and analysis directly from the terminal using standard libraries.

## Tech Stack

* Language: Python 3.x
* Libraries: `argparse`, `sys`
* No database required

## Features

* Reverse text (`--reverse`)
* Convert text to uppercase (`--uppercase`)
* Count words and characters (`--count`)
* Display memory size of text (`--size`)

## How to Run

1. Clone or download the repository.
2. Run the script via terminal or VS Code:

```bash
python textwiz.py "your text here" --uppercase --count
```

## Possible Extensions

* Read text from stdin if no argument is provided
* Add quiet mode to suppress extra messages
* Support additional transformations (lowercase, title-case, etc.)
* Chain multiple transformations in user-specified order

---

See you in the next one!

---
