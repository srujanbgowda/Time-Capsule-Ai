import json
from datetime import datetime

def save_time_capsule(data, unlock_date, filename="time_capsule.json"):
    capsule = {
        "message": data,
        "unlock_date": unlock_date.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(filename, "w") as file:
        json.dump(capsule, file)
    print(f"Time capsule saved! Will unlock on {unlock_date}.")

def load_time_capsule(filename="time_capsule.json"):
    with open(filename, "r") as file:
        capsule = json.load(file)
    
    unlock_date = datetime.strptime(capsule["unlock_date"], "%Y-%m-%d %H:%M:%S")
    current_date = datetime.now()

    if current_date >= unlock_date:
        return capsule["message"]
    else:
        return f"🔒 Capsule is locked until {unlock_date}."

# Example usage:
if __name__ == "__main__":
    choice = input("Do you want to (1) create or (2) open the time capsule? ")

    if choice == "1":
        user_input = input("Enter your AI input/message: ")
        date_str = input("Enter unlock date (YYYY-MM-DD HH:MM:SS): ")
        unlock_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        save_time_capsule(user_input, unlock_dt)
    elif choice == "2":
        result = load_time_capsule()
        print(result)
    else:
        print("Invalid choice.")
