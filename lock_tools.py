# lock_tools.py


def is_locked(failed, max_tries=3):
    """Return True if failed is max_tries or more, else False."""
    return failed >= max_tries


def tries_left(failed, max_tries=3):
    """Return 0 if the account is locked, else max_tries - failed."""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed):
    """Return 'locked', or 'active (N tries left)'."""
    if is_locked(failed):
        return "locked"
    left = tries_left(failed)
    return f"active ({left} tries left)"


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))

