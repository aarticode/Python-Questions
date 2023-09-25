#change the global variable with the global keyword
x = 100

def myfunc():
  x = 100


print(x)

#python output varibale
x = 10
y = 15
z = 20
print(x, y, z)

#local of python varibale

#loacl scope
def demo():
    a=100
    print(a)

    #call
demo()

#create python variable

a=10
b="Aarti"
c=35

print(a)
print(b)
print(c)


#In a function, how do you create a global variable?
#We can create a global variable by designating it as global within every function that assigns to it. We can utilize it in other functions.

global_var = 0
def modify_global_var():
 global global_var # Setting global_var as a global variable
 global_var = 10
def printing_global_var():
 print(global_var) # There is no need to declare global variable
modify_global_var()
printing_global_var() # Prints 10


