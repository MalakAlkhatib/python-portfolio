# session_timer.py

# 1 & 2. Ask for input and convert to integer
total_seconds = int(input("Session length in seconds: "))

# 3. Calculate minutes and remaining seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# 4. Print the formatted result
print(f"Session length: {minutes} minutes and {seconds} seconds")

# 5. Test results:
# Test 905 -> Session length: 15 minutes and 5 seconds
# Test 60  -> Session length: 1 minutes and 0 seconds
# Test 59  -> Session length: 0 minutes and 59 seconds

