class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        self.passwords[website] = {"username": username, "password": password}
        print(f"✅ Password for {website} saved successfully.")

    def view_password(self, website):
        if website in self.passwords:
            print(f"Website: {website}")
            print(f"Username: {self.passwords[website]['username']}")
            print(f"Password: {self.passwords[website]['password']}")
        else:
            print(f"❌ No password saved for {website}.")

    def list_all(self):
        if not self.passwords:
            print("📭 No passwords saved.")
        else:
            print("🔐 Stored Websites:")
            for site in self.passwords:
                print(f"- {site}")

def print_sep():
    print("=" * 40)

def main():
    manager = PasswordManager()

    while True:
        print_sep()
        print("Welcome to the Password Manager")
        print_sep()
        print("1. Add a password")
        print("2. View a password")
        print("3. List all saved websites")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Enter website name: ")
            username = input("Enter username/email: ")
            password = input("Enter password: ")
            manager.add_password(website, username, password)

        elif choice == "2":
            website = input("Enter website name to view password: ")
            manager.view_password(website)

        elif choice == "3":
            manager.list_all()

        elif choice == "4":
            print("🔒 Exiting Password Manager. Stay safe!")
            break

        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
