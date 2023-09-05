#Write a function that checks if two given strings are anagrams of each other. Anagrams are words or phrases formed by rearranging the letters of another.
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase for comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters in both strings are the same
    return sorted(str1) == sorted(str2)

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("Hello", "World"))     # False
print(are_anagrams("Astronomer", "Moon starer"))  # True