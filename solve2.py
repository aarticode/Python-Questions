

#Question: Write a Python function to reverse the order of words in a given sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

# Test the function
sentence = "Hello world! Python is awesome."
result = reverse_sentence(sentence)
print(result)







class Calculator:
    def add(self, *args):
        return sum(args)

# Create an object
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9


#What does len() do?
#len() is an inbuilt function used to calculate the length of sequences like list, python string, and array.

my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)

# How to remove values to a python array?
#Elements can be removed from a python array by using pop() or remove() methods.

#pop(): This function will return the removed element .

#remove():It will not return the removed element
import array

x = array.array('d', [8.1, 2.4, 6.8, 1.1, 7.7, 1.2, 3.6])
print(x.pop())
print(x.pop(3))
x.remove(8.1)
print(x)


#Python if else Statement:

def main():
    x, y = 2, 8

    if (x < y):
        st = "x is less than y"
    print(st)


if __name__ == "__main__":
    main()

 #Explain While loop in Python with example
#While loop does the exact same thing what “if statement” does, but instead of running the code block once, they jump back to the point where it began the code and repeat the whole process again.

x=0
#define a while loop
while(x <4):
        print(x)
        x = x+1

#Enumerate() in Python is a built-in function used for assigning an index to each item of the iterable object. It adds a loop on the iterable objects while keeping track of the current item and returns the object in an enumerable form. This object can be used in a for loop to convert it into a list by using list() method.
# use a for loop over a collection
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)

# use the break and continue statements

# for x in range (10,20):
# if (x == 15): break
# if (x % 5 == 0) : continue
# print x


#How can you use for loop to repeat the same statement over and again?
#You can use for loop for even repeating the same statement over and again. Here in the example, we have printed out the word “guru99” three times
for i in '123':
 print ("guru99",i,)

#Removing  All whitespace in String

import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

#Counting a whitspace in  a string

string = "P r ogramm in g "
print(string.count(' '))


#Randimizing the items of a list in Python

from random import shuffle

lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)







