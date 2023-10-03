#Question: Write a Python function to reverse the order of words in a given sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

# Test the function
sentence = "Hello world! Python is awesome."
result = reverse_sentence(sentence)
print(result)

#Question: Write a Python function to remove duplicate elements from a given list.

def remove_duplicates(lst):
    return list(set(lst))

# Test the function
numbers = [1, 2, 3, 3, 4, 4, 5, 6, 6]
result = remove_duplicates(numbers)
print(result)





