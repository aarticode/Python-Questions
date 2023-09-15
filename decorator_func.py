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



