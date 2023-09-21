# Define the decorator_func decorator
def decorator_func(func):
    def wrapper_func():
        print("wrapper_func worked")
        return func()
    print("decorator_func worked")
    return wrapper_func

# Define the show function
def show():
    print("show worked")

# Apply the decorator_func decorator to the show function
decorator_show = decorator_func(show)

# Call the decorated show function
decorator_show()

def decorator_lowercase(function):   # defining a Python decorator
    def wrapper():
        result = function()
        result_lowercase = result.lower()
        return result_lowercase
    return wrapper
@decorator_lowercase ## calling the decorator
def intro():                     # Normal function
    return 'Hello, I AM AARTI'

print(intro())





