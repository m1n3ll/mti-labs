# Procedural 
def factorial(n):
    if n == 0:            
        return 1
    else:                
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial (Procedural):", factorial(num))


# Functional 

from functools import reduce

def factorial_func(n):
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)

num = int(input("Enter a number: "))
print("Factorial (Functional):", factorial_func(num))
