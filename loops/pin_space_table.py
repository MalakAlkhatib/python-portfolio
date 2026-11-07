# pin_space_table.py
# Calculate time needed to guess PINs of length 4 to 8.

GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    pins = 10 ** digits
    seconds = pins // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // (60 * 24)
    print(f"{digits} digits: {pins} PINs, {minutes} minutes, {days} days")
