import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def is_strong_password(password):
    # Check if the password meets the complexity requirements
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    return has_upper and has_lower and has_digit and has_special

# Prompt the user for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and validate the password
password = generate_password(length)
while not is_strong_password(password):
    password = generate_password(length)

print("Generated Password:", password)
