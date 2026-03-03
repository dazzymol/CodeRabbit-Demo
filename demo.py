import hashlib
import os

# ❌ 1. Hardcoded credentials (security issue)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


def login(username, password):
    # ❌ 2. Plaintext password comparison
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful")
        return True
    else:
        print("Invalid credentials")
        return True  # ❌ 3. Logic bug (should return False)


def calculate_total(price, quantity):
    # ❌ 4. No input validation (negative values allowed)
    total = price * quantity

    # ❌ 5. Floating point precision issue
    tax = total * 0.0825
    return total + tax


def save_user_data(username, data):
    # ❌ 6. Insecure file handling (no error handling, possible path injection)
    file_path = f"{username}.txt"
    file = open(file_path, "w")
    file.write(str(data))
    file.close()


def hash_password(password):
    # ❌ 7. Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


# ❌ 8. Code execution on import (bad practice)
print(login("admin", "wrongpassword"))
print(calculate_total(-100, 2))
save_user_data("../hack", {"role": "admin"})
