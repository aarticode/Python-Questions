fib = [0,1]
# Range starts from 0 by default
for i in range(5):
    fib.append  (fib[-1] + fib[-2])

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))


# Writing Fibonacci Series


fib = [0,1]

# Range starts from 0 by default
for i in range(6):
    fib.append(fib[-1] + fib[-2])

# Converting the list of integers to string
print(', '.join(str(j) for j in fib))

#Iteration by for loop on the string

s = "Hello World"
for i in s:
	print(i)
