import re


name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")
username = input("Username: ")


if re.fullmatch(r"[A-Za-z ]+", name):
    print("Valid name")
else:
    print("Invalid name")


if re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email):
    print("Valid email")
else:
    print("Invalid email")


if re.fullmatch(r"\d{10}", phone):
    print("Valid phone")
else:
    print("Invalid phone")


if re.fullmatch(r"[A-Za-z0-9_]+", username):
    print("Valid username")
else:
    print("Invalid username")