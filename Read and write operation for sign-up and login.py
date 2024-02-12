import csv

def sign_up(username, password):
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("Sign up successful!")

def login(username, password):
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return True
    print("Invalid username or password. Please try again.")
    return False

def main():
    print("Welcome to the Inventory Management System")

    while True:
        print("\n1. Sign up")
        print("2. Log in")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            sign_up(username, password)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
