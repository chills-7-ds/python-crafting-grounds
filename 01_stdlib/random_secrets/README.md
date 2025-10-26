# 🎲 Random & Secrets — Python Standard Libraries

---

## **Overview**

These two modules power Python’s *randomness* — but for different purposes.

* `random` → generates **pseudo-random** numbers useful for simulations, testing, and games.
* `secrets` → generates **cryptographically secure** randomness for passwords, tokens, and secure selections.

This project explores both through a small CLI tool that demonstrates correct usage and practical understanding — ideal for interviews and foundational learning.

---

## **Goal**

To understand:

1. The **difference** between pseudo-random and secure random generation.
2. How to use both modules correctly in real-world scenarios.
3. Build a minimalist CLI showing each module in action.

---

## **Tech Stack**

* **Language:** Python 3.x
* **Libraries Used:**

  * `random` — for general randomness
  * `secrets` — for cryptographically secure randomness
  * `string` — for character sets (letters, digits, symbols)
* **Interface:** Command-line (CLI)

---

## **Features**

* Generate **secure passwords** with random letters, digits, and punctuation (`secrets.choice()`).
* Generate **simple 6-digit random codes** using pseudo-random integers (`random.randint()`).
* Demonstrates **practical and interview-focused** understanding of both libraries.
* Clean, single-file implementation — no external dependencies.

---

## **How to Run**

**Clone or create the file:**

```bash
git clone <your_repo_url>
cd <folder_name>
```

**Run the script:**

```bash
python secure_generator.py
```

**Then choose an option:**

```
1. Generate Secure Password
2. Generate Random 6-digit Code
```
---

## **Possible Extensions**

* Add an option for **custom password rules** (only letters, only digits, etc.)
* Save generated passwords or tokens to a file (with proper security).
* Add a mode to generate **secure tokens** using `secrets.token_hex()` or `secrets.token_urlsafe()`.
* Create a small **GUI** using Tkinter or a **web interface** using Flask.

---

**Notion Reference:**
🔗 [Random and Secrets – Learning Notes](https://dramatic-psychology-0d8.notion.site/random-and-secrets-29803656c6c380b8ad7af261dd43d7a5?source=copy_link)

---

see you in the next one!