1.#Arithmetic operators perform basic arithmetic operations.
# For example "+" is used to add and "?" is used for subtraction.

# Adding two values
print(12+23)
# Subtracting two values
print(12-23)
# Multiplying two values
print(12*23)
# Dividing two values
print(12/23)

2.#Relational Operators are used to comparing the values.
# These operators test the conditions and then returns a boolean value either True or False.

# Examples of Relational Operators
a, b = 10, 12
print(a==b) # False
print(a<b) # True
print(a<=b) # True
print(a!=b) # True

3.#Assignment operators are used to assigning values to the variables. See the examples below.


# Examples of Assignment operators
a=12
print(a) # 12
a += 2
print(a) # 14
a -= 2
print(a) # 12
a *=2
print(a) # 24
a **=2
print(a) # 576

4.#Logical operators are used to performing logical operations like And, Or, and Not. See the example below.


# Logical operator examples
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not b) # True

5.#Bitwise Operators are used to performing operations over the bits. The binary operators (&, |, OR) work on bits. See the example below.


# Identity operator example
a = 10
b = 12
print(a & b) # 8
print(a | b) # 14
print(a ^ b) # 6
print(~a) # -11

#The Walrus Operator allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don’t want to repeat the calculation.

#The Walrus Operator is represented by the `:=` syntax and can be used in a variety of contexts including while loops and if statements.

names = ["Jacob", "Joe", "Jim"]

if (name := input("Enter a name: ")) in names:
	print(f"Hello, {name}!")
else:
	print("Name not found.")




