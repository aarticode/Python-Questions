#Write a Python function that takes a list of numbers as input
# and returns the sum of all the numbers in the list.
def number(list):
    a=0
    for x in list:
        a=a+x
    return a
print (number([1,2,3,4,5,6,7,8]) )