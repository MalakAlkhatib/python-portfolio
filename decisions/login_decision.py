# login_decision.py

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input()
failed = int(input())
password = input()

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password != STORED_PASSWORD:
    left = MAX_FAILED - failed - 1
    print(f"Access denied. Attempts left: {left}")
else:
    print("Access granted.")
