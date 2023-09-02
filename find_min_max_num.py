#Question: Write a Python function to find the largest and smallest numbers in a given list

def  find_min_max(numbers):
    if not numbers:
       return none
    min_number=numbers[0]
    max_number=numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    return min_number, max_number


# Test the function
nums = [5, 2, 9, 1, 7]
min_num, max_num = find_min_max(nums)
print( f"The smallest number is: {min_num}")
print( f"The largest number is: {max_num}")
