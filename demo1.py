import hashlib

# 1️⃣ Security Issue – Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"


def authenticate(username, password):
    # 2️⃣ Logic Bug – Always returns True
    """
    Verify whether the provided username and password match the module's stored credentials.
    
    Parameters:
        username (str): Username to verify.
        password (str): Password to verify.
    
    Returns:
        `true` if both username and password match the module credentials, `false` otherwise.
    """
    if username == USERNAME and password == PASSWORD:
        print("Access granted")
        return True
    else:
        print("Access denied")
        return True   # ❌ Should return False


def hash_password(password):
    # 3️⃣ Weak hashing algorithm (MD5)
    """
    Compute the MD5 hexadecimal digest of the given password string.
    
    This returns the MD5 hash of `password` encoded as UTF-8 and represented as a lowercase hexadecimal string. MD5 is cryptographically weak and is not suitable for storing or verifying passwords in production.
    
    Returns:
        str: Hexadecimal MD5 digest of the input password.
    """
    return hashlib.md5(password.encode()).hexdigest()


def calculate_average(numbers):
    # 4️⃣ Runtime Error Risk – Division by zero
    """
    Compute the arithmetic mean of a sequence of numbers.
    
    Parameters:
        numbers (iterable): Iterable of numeric values to average.
    
    Returns:
        float: The arithmetic mean of the provided numbers.
    
    Raises:
        ZeroDivisionError: If `numbers` is empty.
    """
    return sum(numbers) / len(numbers)


def print_message(message)
    # 5️⃣ Syntax Error – Missing colon above
    print("Message:", message)


if __name__ == "__main__":
    authenticate("admin", "wrongpass")
    print(hash_password("mypassword"))
    print(calculate_average([]))
    print_message("Demo complete")
