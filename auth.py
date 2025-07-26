# auth.py

users = {
    "admin": "password123",
    "mary": "marypass"
}

current_user = None

def login():
    global current_user
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        current_user = username
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid credentials")
        return False

def logout():
    global current_user
    current_user = None
    print("Logged out successfully.")
