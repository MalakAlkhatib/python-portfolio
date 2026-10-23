# int_research.py
# Gold Task: Researching int() behavior with different strings

# 1. int(" 22 ") -> Works because Python ignores leading/trailing whitespaces.
print(int(" 22 "))

# 2. int("+22") -> Works because Python accepts a leading plus sign.
print(int("+22"))

# 3. int("0022") -> Works because Python handles leading zeros for positive integers.
print(int("0022"))

# 4. int("2_2") -> Fails with ValueError because underscores are not allowed inside string conversions for int().
# print(int("2_2"))

