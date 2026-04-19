
---

# 📁 2. password_manager.py (PASTE THIS)

```python id="pmr6"
import json
import hashlib
import os

DATA_FILE = "data.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_password():
    site = input("Enter website/app name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = load_data()

    data[site] = {
        "username": username,
        "password": hash_password(password)
    }

    save_data(data)
    print("[✓] Password saved securely")


def view_passwords():
    data = load_data()

    if not data:
        print("[!] No saved passwords found")
        return

    for site, info in data.items():
        print(f"\nSite: {site}")
        print(f"Username: {info['username']}")
        print(f"Password (hashed): {info['password']}")


def main():
    while True:
        print("\n🔐 Password Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            break
        else:
            print("[!] Invalid choice")


if __name__ == "__main__":
    main()
