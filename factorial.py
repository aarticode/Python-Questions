#Question: Write a Python function to find the factorial of a given number.#
def fact(n):
    f=1
    for i in range(1,n+1):
        f= f * i
    return f
x=5
result= fact(x)
print(result)

# Python program to find factorial of a given number

#importing the math function
import math

#Defining the factorial() function to find factorial
def factorial(num):
	return(math.factorial(num))


# Input function to get the number from user
num = int(input('Please enter a number to find the factorial: '))

#Printing the factorial of the given number
print("The factorial of the given number", num, "is",
	factorial(num))