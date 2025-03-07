import secrets
import string

def generate_password(length):
    """
    Generates a secure random password of user-defined length (min 8 characters).
    """
    if length < 8:
        print("❌ Password length should be at least 8 characters for security.")
        return None

    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Ask user for password length
try:
    length = int(input("Enter password length (min 8): "))
    password = generate_password(length)

    if password:
        print(f"🔐 Your secure password: {password}")

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")
