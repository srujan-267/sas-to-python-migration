# login_app.py

users = {
    "admin": "admin123",
    "srujan": "python123"
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"\nWelcome {username}!")
        return True
    else:
        print("\nInvalid username or password.")
        return False

def register():
    username = input("Choose a username: ")

    if username in users:
        print("Username already exists.")
        return

    password = input("Choose a password: ")
    users[username] = password

    print("User registered successfully!")

def show_users():
    print("\nRegistered Users:")
    for user in users:
        print("-", user)

while True:
    print("\n===== LOGIN APPLICATION =====")
    print("1. Login")
    print("2. Register")
    print("3. View Users")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login()

    elif choice == "2":
        register()

    elif choice == "3":
        show_users()

    elif choice == "4":
        print("Thank you for using the application.")
        break

    else:
        print("Invalid option. Please try again.")
        print("You have successfully logged in.")
print("Redirecting to dashboard...")
print("Welcome to Srujan's Python Application")