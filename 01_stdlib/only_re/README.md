# **Regex Extractor CLI**

## **Overview**

A lightweight command-line tool built with Python’s `re` (regular expressions) module to extract useful patterns like emails, phone numbers, and dates from a given text file. It demonstrates how text parsing and data cleaning work behind the scenes in automation and preprocessing tasks.

---

## **Goal**

To understand and practically apply the `re` module for pattern recognition — showing how regex can identify, extract, and classify text data efficiently without external dependencies.

---

## **Tech Stack**

**Language:** Python
**Library:** `re` (Regular Expressions module)
**Database:** None — works directly on text files or strings.

---

## **Features**

* Detects and extracts:

  * Email addresses
  * Phone numbers
  * Dates in multiple formats
* Uses flexible regex patterns (non-capturing and group-based)
* Cleanly formatted CLI output showing category-wise results
* Modular design — easy to add new regex patterns for URLs, IPs, etc.

---

## **How to Run**

1. **Clone or download** the project folder.
2. **Open terminal** in the folder.
3. **Run the script** with a sample file or inline text.

   ```bash
   python regex_extractor.py
   ```

   or redirect input:

   ```bash
   python regex_extractor.py < sample.txt
   ```
4. The output will display all extracted matches category-wise.

---

## **Possible Extensions**

* Add regex for URLs, IP addresses, or credit card numbers.
* Export matches to `.csv` or `.json`.
* Add command-line arguments for file input, pattern selection, or output format.
* Integrate color-coded terminal output for category highlighting.

---

**Notion site:** [Regex Extractor - BTS 🔍](https://dramatic-psychology-0d8.notion.site/re-bts-29703656c6c3802ba5e4cdcd29d7d9cb?source=copy_link) 
---

**See you in the next one!**