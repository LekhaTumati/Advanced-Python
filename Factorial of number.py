
def fact(n):

    return 1 if n == 1 or n == 0 else n*fact(n-1)
n = int(input("Enter the number you want to find the factorial of"))
print(fact(n))