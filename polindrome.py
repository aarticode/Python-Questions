#Write a Python function to check if a given string is a palindrome.

a=input("enter string:")
b=a[-1::-1]
if (a==b):
  print("polindrome string")
else:
  print("not polindrome string")

  # write a program to check whether a number is palindrome or not
i = int(input("enter number to check"))
rev = 0
x = i
while (i > 0):
  rev = (rev * 10) + i % 10
  i = i // 10
  if (x == rev):
    print(" number is palindrome ")
  else:
    print("  number is not palindrome")




# Write a Python program to check whether a given string is a palindrome or not, without using an iterative method?
    def fun(string):
      s1 = string
      s = string[::-1]
      if s1 == s:
        return True
      else:
        return False


    print(fun("madam"))



