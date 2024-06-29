import re

def check_password_strength(password):
    password = password.strip()

    if len(password) < 8:
        return "Weak"
        print("Strenghthen your password!")
    elif len(password) >= 8 and len(password) <= 12:
        return "Medium"
        print("You can do better.")
    else:
        return "Strong"

    char_types = {"uppercase": 0, "lowercase": 0, "numbers": 0, "special_chars": 0}

    for char in password:
        if char.isupper():
            char_types["uppercase"] += 1
        elif char.islower():
            char_types["lowercase"] += 1
        elif char.isdigit():
            char_types["numbers"] += 1
        elif not char.isalnum():
            char_types["special_chars"] += 1

    if sum(char_types.values()) < 3:
        return "Weak"

    return "Strong"

password = input("Enter your password: \n")
print(check_password_strength(password))
