# Python program to find the factorial of a number using recursion
def factorial(x):
  if x==0 or x==1:
    return 1
  else:
    return (x*factorial(x-1))
number=int(input("Enter a number: "))
result=factorial(number)
print("The factorial of",number,"is",result)
