# health_tracker.py

# Global health log
health_log = {}

def log_steps():
    try:
        steps = int(input("Enter the number of steps taken: "))
    except ValueError:
        print("Invalid input. Defaulting to 0 steps.")
        steps = 0  
    health_log['steps'] = steps
    return steps

def log_water():
    n = input("Enter water intake in liters [default is 2.0]: ")
    if n.strip() == "":
        n = 2.0
    else:
        try:
            n = float(n)
        except ValueError:
            print("Invalid input. Defaulting to 2.0 liters.")
            n = 2.0
    health_log['water'] = n
    return n

def log_calories(consumed_default=1800, burned_default=400):
    cal = input("Enter calories consumed [default 1800]: ")
    try:
        cal = int(cal)
    except ValueError:
        print("Invalid input. Using default calories consumed.")
        cal = consumed_default

    cal_burned = input("Enter calories burned [default 400]: ")
    try:
        cal_burned = int(cal_burned)
    except ValueError:
        print("Invalid input. Using default calories burned.")
        cal_burned = burned_default

    health_log['calories_consumed'] = cal
    health_log['calories_burned'] = cal_burned
    return cal, cal_burned

def log_activities(*activities):
    if not activities:
        print("No activities logged.")
        return None
    health_log['activities'] = list(activities)
    return activities

def log_activities_input():
    activity_input = input("Enter the activities you've done (comma-separated): ")
    activities = [act.strip() for act in activity_input.split(",") if act.strip()]
    health_log['activities'] = activities
    return activities

def log_custom(**kwargs):
    if not kwargs:
        print("No custom data provided.")
        return None
    health_log['notes'] = kwargs
    return kwargs

filter_short_activities = lambda acts: [a for a in acts if a[1] >= 15]
# Example: [("cycling", 20), ("stretch", 10)] → filters out "stretch"

def ml_to_liters(ml):
    return ml / 1000

def log_heart_rate():
    def get_bpm():
        try:
            return int(input("Enter your heart rate (bpm): "))
        except ValueError:
            print("Invalid input. Defaulting to 70 bpm.")
            return 70
    bpm = get_bpm()
    health_log['heart_rate'] = bpm
    return bpm

def show_summary():
    if not health_log:
        print("No health data available. Please log something first! 📝")
        return

    print("\n📋 Health Summary:")
    for key, value in health_log.items():
        print(f"- {key.replace('_', ' ').capitalize()}: {value}")
    
    print("\n💡 Suggestions:")
    if health_log.get('water', 0) < 2.0:
        print("Drink a bit more water 💧")
    if health_log.get('calories_consumed', 0) > 2200:
        print("Watch the calorie intake 🍔")
    if health_log.get('heart_rate', 0) > 100:
        print("Heart rate's high — maybe take a breather 🧘")

    print("You're doing great! Keep it up! 🚀")
    
if __name__ == "__main__":
    log_steps()
    log_water()
    log_calories()
    log_heart_rate()
    show_summary()
