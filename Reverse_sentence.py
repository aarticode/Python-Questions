#Question: Write a Python function to reverse the order of words in a given sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

# Test the function
sentence = "Hello world! Python is awesome."
result = reverse_sentence(sentence)
print(result)


