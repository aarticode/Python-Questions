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



# Write a Python program to check if a given positive integer is a prime number or not.
def is_prime(n):
    if n <= 1:
        return False  # 1 and non-positive integers are not prime

    if n == 2:
        return True   # 2 is a prime number

    if n % 2 == 0:
        return False  # All other even numbers are not prime

    # Check for divisibility by odd numbers from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # n is divisible by a number other than 1 and itself

    return True  # If no divisors are found, n is prime

# Example usage:
num = int(input("Enter a positive integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

