# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1: Moving failed counter outside the loop so it doesn't reset to 0 in each iteration
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 & 3: Using float division '/' to get 30.0 and moving print outside the loop
print(f"Average session: {total / count} minutes")

# Bug 4: Changing range(1, 4) to range(1, 5) so it includes Level 4
for level in range(1, 5):
    print(f"Level {level}")