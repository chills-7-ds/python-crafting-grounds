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

## Extended Project Docs on Notion

For behind-the-scenes thought processes((hints, expected output, aha moments)), future improvements, project roadmap, and helpful resources and references, check out the dedicated Notion site:[[link-to-notion-doc](https://dramatic-psychology-0d8.notion.site/argparse-sys-project-28d03656c6c38083979bf26e429009e2?source=copy_link)]

See you in the next one!
---