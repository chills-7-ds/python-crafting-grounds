# Health Tracker 🩺

# Overview  
A simple yet function-packed personal health tracking CLI app built with pure Python. This project helps log your daily physical activities, calories, water intake, and more — while exploring different types of Python functions with real-world relevance.

# Goal  
To demonstrate the usage of all core function types in Python — including default arguments, `*args`, `**kwargs`, lambdas, nested functions, and helper methods — through a hands-on health logging utility.

# Tech Stack  
- Language: Python 🐍  
- Libraries: None (Standard I/O only)  
- Database: Just a spicy global dictionary `health_log`  

# Features  
- `log_steps()` → Log daily step count  
- `log_water()` → Track water intake with default fallback  
- `log_calories()` → Log calories consumed & burned (with optional defaults)  
- `log_activities(*args)` → Use `*args` to log multiple activities  
- `log_activities_input()` → Alt input method for comma-separated values  
- `log_custom(**kwargs)` → Log custom notes like mood, sleep via `**kwargs`  
- `filter_short_activities = lambda ...` → Use lambda to filter low-effort sessions  
- `ml_to_liters()` → Convert milliliters to liters (helper converter)  
- `log_heart_rate()` → Nested function example for BPM logging  
- `show_summary()` → Output health report + intelligent suggestions  
- **BONUS:** Global `health_log` dictionary for easy state management (- A global health log is just a variable (like a dictionary) that’s defined outside any function, so that all functions can access and update it.)

# How to Run  
1. Clone the repo  
```bash
   git clone https://github.com/yourusername/healthtrackr.git
   cd healthtrackr
````
```

2. Run it using Python

```bash
   python3 healthtrackr.py
```

# Possible Extensions

* **`weekly_summary()`**: Accept a list of 7 `health_log`-style dictionaries and compute average steps, water, calories, etc. Great for tracking weekly consistency.
* Add file logging or export to `.csv`
* Integrate with speech-to-text for faster input
* Hook into an API like Fitbit or Apple Health
* Add unit tests for individual logging functions

---
# Extended Project Docs on Notion
* For behind-the-scenes thought processes((hints, expected output, aha moments)), future improvements, project roadmap, and helpful resources and references, check out the dedicated Notion site: https://dramatic-psychology-0d8.notion.site/Health-tracker-doc-bts-20b03656c6c3809088b6dfc1f1a14f15?source=copy_link

**See you in the next one! **
