#In Python, what is a negative index?
#In Arrays and Lists, Python contains a unique feature called negative indexing. Python starts indexing from the beginning of an array or list in a positive integer but reads items from the ending of an array or list in a negative index.

import array
a = [4, 6, 8, 3, 1, 7]
print(a[-3])
print(a[-5])
print(a[-1])


#from array import*
#arrayname =array(Typecode,[initializers])

import array as arr
a = arr.array('i',[2,4,6,8])
print ("first element:" ,a[0])
print ("second element:",a[1])
print ("third element:",a [2])
