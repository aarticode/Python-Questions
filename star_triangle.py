#Write a program in Python to produce Star triangle?
#The below code produces a star triangle-

def Star_triangle(n):
    for x in range(n):
        print(' '*(n-x-1)+'*'*(2*x+1))

Star_triangle(9)

#Write a program to print different star patterns

n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(n):
        for j in range(i, n):
            print(' ', end=' ')
        for j in range(i):
            print('*', end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print()



#Building a Pyramid in Python
floors = 3
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

