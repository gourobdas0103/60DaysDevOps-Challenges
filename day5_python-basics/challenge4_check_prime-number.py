def is_prime(number):
    """
    Checks if a given number is a prime number.
    """
    if number < 2:
        return False  # Numbers less than 2 are not prime

    for i in range(2, int(number ** 0.5) + 1):  # Check divisibility up to √number
        if number % i == 0:
            return False  # If divisible, it's not prime

    return True  # If no divisors found, it's prime

# Ask the user for input
try:
    num = int(input("Enter a number: "))

    # Check and print result
    if is_prime(num):
        print(f"✅ {num} is a prime number.")
    else:
        print(f"❌ {num} is not a prime number.")

except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")