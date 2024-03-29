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
print ("third element:", a [2])


class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums





# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)



#Python Program to Find Sum of Array
#Iterating through the array and adding each element to the sum variable and finally displaying the sum.

# main function
if __name__ == "__main__":
	# input values to list
	arr = [12, 3, 4, 15]

	# calculating length of array
	n = len(arr)
	# calling function ans store the sum in ans
	ans = _sum(arr)
	# display sum
	print('Sum of the array is ', ans)

#Python Program to Find Sum of Array Using enumerate function
#This code calculates the sum of elements in the list list1 using a loop. It iterates through each element, adds it to the running sum s, and then prints the final sum.

list1 = [12, 4, 4, 15];s=0
for i,a in enumerate(list1):
 s+=a
print(s)



