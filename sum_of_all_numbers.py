#Write a Python function that takes a list of numbers as input
# and returns the sum of all the numbers in the list.
def number(list):
    a=0
    for x in list:
        a=a+x
    return a
print (number([1,2,3,4,5,6,7,8]))


 #Write a Python program to calculate the sum of a list of numbers?
def sum(num):
    if len(num) == 1:
        return num[0]  # With only one element in the list, the sum result will be equal to the element.
    else:
        return num[0] + sum(num[1:])

print(sum([2, 4, 5, 6, 7]))


#write a program to pick any two number and add them,which results in the sum=11
numbers = [1, 3, 4, 5, 6, 7, 9, 6]
target_sum = 11

def find_numbers_with_sum(numbers, target_sum):
    # Iterate through the list of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Avoid picking the same number twice
            if numbers[i] + numbers[j] == target_sum:
                return numbers[i], numbers[j]
    return None  # If no pair with the target sum is found

result = find_numbers_with_sum(numbers, target_sum)

if result:
    num1, num2 = result
    print(f"The two numbers that sum to {target_sum} are {num1} and {num2}.")
else:
    print(f"No two numbers sum to {target_sum} in the list.")
