def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, the number is not prime

    return True  # No factors found, the number is prime

# Test cases
print(is_prime(2))      # True (2 is prime)
print(is_prime(17))     # True (17 is prime)
print(is_prime(9))      # False (9 is not prime)
print(is_prime(1))      # False (1 is not prime)
print(is_prime(25))     # False (25 is not prime)
