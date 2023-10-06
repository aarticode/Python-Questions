1. #Why use else in try/except construct in Python?
#`try:` and `except:` are commonly known for exceptional handling in Python, so where does `else:` come in handy? `else:` will be triggered when no exception is raised
try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))
    Addition = num1+num2
    print(f'Result is: {Addition}')
except:
    print('Invalid input!')
else:
    print('Addition is successful.')


## Try 1 ##
# Enter Numerator: 2
# Enter Denominator: d
# Invalid input!

## Try 2 ##
# Enter Numerator: 2
# Enter Denominator: 1
# Result is: 2.0
# Division is successful.



2.#Write a Python program to calculate the sum of a list of numbers?
def sum(num):
    if len(num) == 1:
        return num[0]  # With only one element in the list, the sum result will be equal to the element.
    else:
        return num[0] + sum(num[1:])

print(sum([2, 4, 5, 6, 7]))

def sum ():
    a=10
    b=20
    c=a+b
    return c
#calling sum function in print statement

print ("The sum is:",sum())


value =5
def func():
    value = 15
    print (value,end=" ")
func()
print (value)




