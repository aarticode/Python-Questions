

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


