# fix_the_record.py
# This program prints a short record about a network device.

device_name = "edge-router"

# Syntax error: variable name cannot start with a number
second_ip = "192.0.2.1"

# Syntax error: 'class' is a reserved keyword in Python
device_class = "router"

# Runtime error: cannot convert letters to int, changed to "22"
port = int("22")

# Runtime error: variable name was misspelled (missing 'e' in device_name)
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", device_class)
print("Port:", port)

# Python detects syntax errors first before running any code because it checks the whole file structure.
