# security_toolkit.py

MIN_LENGTH = 8


def border(width):
    """Print + then width + 2 dashes, then +."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a box."""
    width = len(text)
    border(width)
    print(f"| {text} |")
    border(width)


def show_menu():
    """Print the title SECURITY TOOLKIT, then the four menu lines."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return invalid if below 0 or above 65535, else system, user, or dynamic."""
    if port < 0 or port > 65535:
        return "invalid"
    if port <= 1023:
        return "system"
    if port <= 49151:
        return "user"
    return "dynamic"


def check_port():
    """Ask Port:, then show Port <port>: <range> in a box."""
    port = int(input("Port: "))
    category = port_range(port)
    show_box(f"Port {port}: {category}")


def password_problem(password, username):
    """Return the first problem: too short (at least 8), then same as the username."""
    if len(password) < MIN_LENGTH:
        return "too short (at least 8)"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask Username: and Password:, show Rejected: <problem> or Password accepted."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem == "":
        show_box("Password accepted")
    else:
        show_box(f"Rejected: {problem}")


def days_to_guess(digits, per_second):
    """Return whole days to try every PIN."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask PIN digits: and Guesses per second:, show <digits> digits: <days> days."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


show_menu()
checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        show_box(f"Checks done: {checks}")
        break
    else:
        print("Unknown choice.")

