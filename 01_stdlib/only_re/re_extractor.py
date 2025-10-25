import re

# ----- 1️⃣ INPUT -----
text = """
Hello, you can contact us at info@company.com or sales@market.io.
Our support number is +91-9876543210 or 040-22446688.
The next meeting is scheduled for 21/10/2025 and another on 2025-11-05.
"""

# ----- 2️⃣ PATTERNS -----
patterns = {
    "Emails": r"[\w\.-]+@[\w\.-]+\.\w+",
    "Phone Numbers": r"(?:\+?\d{1,3}[-\s]?)?(?:\d{2,4}[-\s]?)?\d{6,10}",
    "Dates": r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b"
}

# ----- 3️⃣ EXTRACTION -----
for label, pattern in patterns.items():
    results = re.findall(pattern, text)
    print(f"\n🔹 {label}:")
    if results:
        for r in results:
            print("  -", r)
    else:
        print("  No matches found.")