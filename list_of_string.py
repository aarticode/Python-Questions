#Write a Python function that takes a list of strings as input and
# returns a new list containing only the strings that start with the
# letter 'A' (case-insensitive). For example, if the input list is
# ['apple', 'banana', 'Avocado', 'orange'], the function should return ['apple', 'Avocado'].
def fruit(list):
    a=[]
    for i in list:
        if i[0].lower()=="a":
            a.append(i)
    return a
list=['apple', 'banana', 'Avocado', 'orange']
print(fruit(list))