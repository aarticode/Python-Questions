# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

fname=input("enter first name: ")
lname=input("enter last name: ")
print("Hello "+lname+" "+fname)


#Write a Python function that takes a string as input and returns
# the reverse of that string. For example, if the input is "Hello, World!",
# the function should return "!dlroW ,olleH".
def reverse(string):
    n=""
    for b in string:
        print (b)
        n=b+n
    return n
print (reverse("AARTI,chouhan"))
