import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        charset = string.ascii_letters + string.digits
    elif complexity == "medium":
        charset = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        charset = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    else:
        print("Invalid complexity choice")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    return password


length = int(input("Enter the length of the password: "))
complexity = input("Enter complexity (low, medium, high): ")

password = generate_password(length, complexity)
if password:
    print("Generated password: " + password)