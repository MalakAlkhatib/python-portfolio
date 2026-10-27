
# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Fix 1 (syntax): added colon at the end of the line
if len(password) < MIN_LENGTH:
    print("- Too short.")
# Fix 2 (semantic): changed '=' to '==' to compare values
elif password == username:
    print("- Same as the username.")

# Fix 3 (semantic): reordered conditions to check >= 16 first
# Fix 4 (semantic): fixed the condition logic for acceptable length
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")
