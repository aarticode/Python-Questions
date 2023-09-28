#In Python, what is a negative index?
#In Arrays and Lists, Python contains a unique feature called negative indexing. Python starts indexing from the beginning of an array or list in a positive integer but reads items from the ending of an array or list in a negative index.

import array
a = [4, 6, 8, 3, 1, 7]
print(a[-3])
print(a[-5])
print(a[-1])

#What is the difference between Python Arrays and lists?
import array
a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
a = array.array('i', [1, 2, 'string'])    #OUTPUT: TypeError: an integer is required (got type str)
a = [1, 2, 'string']
for i in a:
   print(i, end=' ')