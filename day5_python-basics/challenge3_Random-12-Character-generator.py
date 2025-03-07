import random
import string

def generate_password(length=12):
    """
    Generates a random password with uppercase, lowercase, digits, and special characters.
    """
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Generate and print the password
random_password = generate_password()
print("🔑 Generated Password:", random_password)