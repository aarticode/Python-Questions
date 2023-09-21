#Write a program to produce Fibonacci series in Python?
#The Fibonacci series refers to a series where an element is the sum of two elements prior to it.

n = int(input("number of terms? "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1