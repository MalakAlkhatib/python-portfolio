# Citation: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# Prediction: False - Empty strings are treated as falsy.
print(bool(""))

# Prediction: True - Non-empty strings are always truthy, even if the text is "0".
print(bool("0"))

# Prediction: False - Integer zero is falsy.
print(bool(0))

# Prediction: False - Float zero is falsy.
print(bool(0.0))

# Prediction: True - Non-empty strings are truthy, even if the text is "False".
print(bool("False"))



