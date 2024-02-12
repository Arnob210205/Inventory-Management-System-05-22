import csv
import os
import hashlib

def hash_password(password):
    # Hash the password before storing it
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up(username, password):
    # Check if the user already exists
    if os.path.exists("users.csv"):
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    print("Username already exists. Please choose a different one.")
                    return

    # Hash the password before storing
    hashed_password = hash_password(password)
    
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])
    print("Sign up successful!")

def login(username, password):
    if not os.path.exists("users.csv"):
        print("No users found. Please sign up first.")
        return False
    
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == hash_password(password):
                print("Login successful!")
                return True
    print("Invalid username or password. Please try again.")
    return False
