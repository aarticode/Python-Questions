#Write a Python function that takes a list of integers as input and returns a
# new list containing only the even numbers from the input list. For exampion should return [2, 4, 6]le,
# if the input list is [1, 2, 3, 4, 5, 6], the funct.
def even(list):
    a=[]
    for i in list:
        if i%2==0:
            a.append(i)
    return a
list=[1,2,3,4,5,6,7,8]
print(even(list))