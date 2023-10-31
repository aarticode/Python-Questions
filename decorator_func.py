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


def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print(intro())





