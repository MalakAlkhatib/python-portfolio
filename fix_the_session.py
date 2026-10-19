# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")

# Fix 1 (runtime error): Convert input string to integer using int()
total_seconds = int(input("Session length in seconds: "))

# Fix 2 (runtime error/semantic): Use integer division // instead of float division /
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
print(f"User: {username}")

# Fix 3 & 4 (semantic errors): Correct output formatting to match the goal output
print(f"Session: {minutes} min {seconds} s")
print("=" * 30)
   