# 🌍 **World Event Countdown Tracker**

---

## 📌 **Overview**

A simple, interactive Python tool that shows exactly **how much time is left** until any event you care about — *with proper timezone awareness*.
It converts your local event time to **UTC** and multiple major cities, so you always know *when* the moment happens *globally*.

---

## 🎯 **Goal**

To **demonstrate real-world use** of Python’s `datetime` and `zoneinfo` modules for:

* Handling timezone-aware datetimes.
* Doing reliable time math with `timedelta`.
* Understanding how the same instant appears in different parts of the world.

This project makes the idea of *“time is relative”* concrete — especially useful for global meetings, launches, or travel planning.

---

## ⚙️ **Tech Stack**

* **Language:** Python 3.9+

* **Libraries:**

  * `datetime` (standard library)
  * `zoneinfo` (standard library)
  * (Optional: `dateutil` for extra parsing power)

* **Database:** None — pure script!

---

## ✨ **Features**

✅ Takes **event name**, **date**, **time**, and **timezone** from the user.
✅ Creates a **timezone-aware datetime**.
✅ Converts event time to:

* UTC
* New York
* London
* Tokyo

✅ Calculates the **time remaining** until the event.
✅ Displays results in clear, human-readable format.

---

## 🚀 **How to Run**

1. Clone or download the script:

   ```bash
   git clone <your-repo-url>
   cd world-countdown-tracker
   ```

2. Run it:

   ```bash
   python world_countdown.py
   ```

3. Follow the prompts:

   * Enter event name, date, time, and timezone.
   * See your event’s timeline across the globe and how long you have left.

---

## 🔮 **Possible Extensions**

* Save multiple events to a local file (JSON or CSV).
* Add **live countdown** that updates every second.
* Support fuzzy date parsing with `dateutil`.
* Add support for sending notifications or reminders.
* Build a simple **web version** with Flask or Streamlit.

---

# Extended Project Docs on Notion
* For behind-the-scenes thought processes((hints, expected output, aha moments)), future improvements, project roadmap, and helpful resources and references, check out the dedicated Notion site:{https://dramatic-psychology-0d8.notion.site/Datetime-project-22f03656c6c380ce9878db59b0628cb6?pvs=73}


**See you in the next one! **