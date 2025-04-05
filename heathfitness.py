class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.workouts = []

class Workout:
    def __init__(self, date, duration, exercises):
        self.date = date
        self.duration = duration
        self.exercises = exercises    

class FitnessApp:
    def __init__(self):
        self.users = []       

    def register_user(self, username, email, password):
        new_user = User(username, email, password)
        self.users.append(new_user)   
        return new_user

    def log_workout(self, user, date, duration, exercises):
        new_workout = Workout(date, duration, exercises)
        user.workouts.append(new_workout)

def print_sep():
    print("=" * 40)

def main():
    fitness_app = FitnessApp()
    while True:
        print_sep()
        print("Welcome to Fitness App")
        print_sep()   
        print("1. Register\n2. Log workout\n3. Exit")   

        choice = input("Select an option: ")     
        if choice == "1":
            username = input("Enter your name: ")
            email = input("Enter email: ")
            password = input("Enter your password: ")
            fitness_app.register_user(username, email, password)
            print_sep()
            print("User registered successfully.")

        elif choice == "2":
            if not fitness_app.users:
                print_sep()
                print("⚠️ No users registered. Please register first.")
                continue

            username = input("Enter your name to log a workout: ")   
            user = next((u for u in fitness_app.users if u.username == username), None)

            if user:
                date = input("Enter workout date (YYYY-MM-DD): ")
                try:
                    duration = int(input("Enter workout duration (minutes): "))
                except ValueError:
                    print("Please enter a valid number for duration.")
                    continue

                exercises = input("Enter exercises (comma-separated): ").split(',')
                fitness_app.log_workout(user, date, duration, exercises)
                print_sep()
                print(f"✅ Workout logged successfully for {username} on {date}")
            else:
                print_sep()
                print(f"❌ User '{username}' not found. Please register first.")

        elif choice == "3":
            print_sep()  
            print("Exiting the fitness app. Goodbye!")   
            break 

        else:
            print_sep()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":   
    main()
