# 🏦 Bank Simulator

# Overview

A beginner-friendly mock bank simulator built in Python that handles account creation, deposits, withdrawals, and balance checks — all with clean, layered error handling. It’s a terminal-based model of basic banking operations, helping you simulate real-world finance logic in a safe sandbox.

# Goal

To demonstrate the core concepts of **error handling**, **loops**, and **functions** in Python through a practical scenario. Focus is on catching user mistakes (like invalid numbers, empty names, and duplicate accounts) without crashing the app and structuring a clean, menu-based CLI application.

# Tech Stack

* **Language**: Python 3
* **Libraries**: None (standard built-in only)
* **Database**: In-memory dictionary (can extend to file-based persistence)

# Features

* Create new bank accounts.
* Deposit money into existing accounts.
* Withdraw with balance check.
* Check account balance.
* Menu-driven CLI with structured exception handling for every input/action.
* Centralized account storage using a dictionary.
* Prevents negative deposits and withdrawals.

# How to Run

```bash
# Clone the repo 
git clone <your-repo-url>
cd banksim/

# Run the simulator
python bank_simulator.py
```

# Possible Extensions

* 📝 **Add file saving** to make accounts persist even after restarting the program
* 🎨 **Make a fancier menu UI** using `rich` or `curses` for improved user interaction
* 🔐 **Add PIN/password logic** for account-level authentication

---
# Extended Project Docs on Notion
* For behind-the-scenes thought processes((hints, expected output, aha moments)), future improvements, project roadmap, and helpful resources and references, check out the dedicated Notion site: https://dramatic-psychology-0d8.notion.site/bank-simulator-doc-bts-20b03656c6c38021bd4df92060370b65?source=copy_link (i also included my own terminal output so do check it out)

**See you in the next one!** 🧠💸