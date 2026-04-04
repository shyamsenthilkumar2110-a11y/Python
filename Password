import json
import base64
import getpass


# ---------- Encryption ----------
def encrypt_password(password):
    encoded = base64.b64encode(password.encode()).decode()
    return encoded


def decrypt_password(encoded_password):
    decoded = base64.b64decode(encoded_password.encode()).decode()
    return decoded


# ---------- File Handling ----------
def load_data():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(manager):
    with open("passwords.json", "w") as file:
        json.dump(manager, file)


# ---------- Features ----------
def add_password(manager):
    site = input("Enter website: ")
    password = getpass.getpass("Enter password (hidden): ")

    encrypted = encrypt_password(password)
    manager[site] = encrypted

    save_data(manager)
    print("Password saved securely!\n")


def view_passwords(manager):
    if not manager:
        print("No passwords stored.\n")
        return

    print("\nStored Websites:")
    for site in manager:
        print(site)
    print()


def search_password(manager):
    site = input("Enter website to search: ")

    if site in manager:
        decrypted = decrypt_password(manager[site])
        print(f"Password for {site}: {decrypted}\n")
    else:
        print("No password found\n")


# ---------- Main ----------
def main():
    manager = load_data()

    while True:
        print("1. Add Password")
        print("2. View Websites")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_password(manager)
            case "2":
                view_passwords(manager)
            case "3":
                search_password(manager)
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid choice\n")


if __name__ == "__main__":
    main()