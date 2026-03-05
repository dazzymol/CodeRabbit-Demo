import hashlib
import os

# ❌ 1. Hardcoded credentials (security issue)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


def login(username, password):
    # ❌ 2. Plaintext password comparison
    """
    Authenticate the given username and password against the module's hardcoded admin credentials.
    
    Prints "Login successful" when credentials match and "Invalid credentials" when they do not.
    Returns:
        True if the provided username and password match the hardcoded admin credentials; due to a logic error, also returns `True` when the credentials do not match.
    """
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful")
        return True
    else:
        print("Invalid credentials")
        return True  # ❌ 3. Logic bug (should return False)


def calculate_total(price, quantity):
    # ❌ 4. No input validation (negative values allowed)
    """
    Compute the total amount for a purchase by applying an 8.25% tax to price multiplied by quantity.
    
    Parameters:
        price (float): Unit price of a single item.
        quantity (int | float): Number of units to purchase.
    
    Returns:
        total_with_tax (float): The final amount equal to (price * quantity) + 8.25% tax on that product.
    """
    total = price * quantity

    # ❌ 5. Floating point precision issue
    tax = total * 0.0825
    return total + tax


def save_user_data(username, data):
    # ❌ 6. Insecure file handling (no error handling, possible path injection)
    """
    Write the string representation of `data` to a file named "<username>.txt", creating or overwriting that file.
    
    Parameters:
        username (str): Base name used to construct the output file as "<username>.txt".
        data (Any): Value to be written; will be converted to a string via `str()` before writing.
    """
    file_path = f"{username}.txt"
    file = open(file_path, "w")
    file.write(str(data))
    file.close()


def hash_password(password):
    # ❌ 7. Weak hashing algorithm (MD5)
    """
    Compute the MD5 hex digest of the given password.
    
    Parameters:
        password (str): The password to hash.
    
    Returns:
        str: MD5 hash of `password` as a lowercase hexadecimal string.
    """
    return hashlib.md5(password.encode()).hexdigest()


# ❌ 8. Code execution on import (bad practice)
print(login("admin", "wrongpassword"))
print(calculate_total(-100, 2))
save_user_data("../hack", {"role": "admin"})
