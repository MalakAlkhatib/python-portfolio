# Ten Conditional Tests
user = "analyst"
role = "viewer"
failed = 3
port = 22

# Test 1 (True) - ==
print("Is user == 'analyst'? I predict True.")
print(user == "analyst")

# Test 2 (True) - !=
print("\n Is role != 'admin'? I predict True.")
print(role != "admin")

# Test 3 (True) - <
print("\n Is failed < 5? I predict True.")
print(failed < 5)

# Test 4 (True) - >=
print("\n Is port >= 22? I predict True.")
print(port >= 22)

# Test 5 (True) - and
print("\n Is user == 'analyst' and port == 22? I predict True.")
print(user == "analyst" and port == 22)

# Test 6 (False) - ==
print("\n Is role == 'admin'? I predict False.")
print(role == "admin")

# Test 7 (False) - >
print("\n Is failed > 10? I predict False.")
print(failed > 10)

# Test 8 (False) - <=
print("\n Is port <= 20? I predict False.")
print(port <= 20)

# Test 9 (False) - or
print("\n Is user == 'root' or role == 'admin'? I predict False.")
print(user == "root" or role == "admin")

# Test 10 (False) - not
print("\n Is not (failed == 3)? I predict False.")
print(not (failed == 3))

