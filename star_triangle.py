#Write a program in Python to produce Star triangle?
#The below code produces a star triangle-

def Star_triangle(n):
    for x in range(n):
        print(' '*(n-x-1)+'*'*(2*x+1))

Star_triangle(9)