n = int(input("enter a number:"))
fact = 1
if (n<0):
  print("sorry, factorial does not exist for negative numbers")
else:
  for i in range(1, n+1):
    factorial = factorial*i
  print("the factorial of ", n,"is", factorial)
