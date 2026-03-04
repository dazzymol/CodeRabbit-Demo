import hashlib

# 1️⃣ Security Issue – Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


def login(username, password):
    # 2️⃣ Logic Error – Incorrect return value
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return True   # ❌ Should return False


def calculate_average(numbers):
    # 3️⃣ Runtime Risk – Division by zero possible
    return sum(numbers) / len(numbers)


def hash_password(password):
    # 4️⃣ Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def print_message(message)
    # 5️⃣ Syntax Error – Missing colon above
    print("Message:", message)


if __name__ == "__main__":
    login("admin", "wrongpass")
    print(calculate_average([]))
    print(hash_password("secret"))
    print_message("Demo complete")
