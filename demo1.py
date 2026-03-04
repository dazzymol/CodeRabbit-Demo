import hashlib

# 1️⃣ Security Issue – Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"


def authenticate(username, password):
    # 2️⃣ Logic Bug – Always returns True
    if username == USERNAME and password == PASSWORD:
        print("Access granted")
        return True
    else:
        print("Access denied")
        return True   # ❌ Should return False


def hash_password(password):
    # 3️⃣ Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def calculate_average(numbers):
    # 4️⃣ Runtime Error Risk – Division by zero
    return sum(numbers) / len(numbers)


def print_message(message)
    # 5️⃣ Syntax Error – Missing colon above
    print("Message:", message)


if __name__ == "__main__":
    authenticate("admin", "wrongpass")
    print(hash_password("mypassword"))
    print(calculate_average([]))
    print_message("Demo complete")
