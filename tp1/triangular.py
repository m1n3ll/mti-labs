# Procedural 

def triangular_number(n):
    if n == 1:             
        return 1
    else:                   
        return n + triangular_number(n - 1)

# Test
N = 5
print("Triangular number (Procedural):", triangular_number(N))


# Functional

from functools import reduce


def triangular_number_func(n):
    return reduce(lambda a, b: a + b, range(1, n + 1))

# Test
N = 5
print("Triangular number (Functional):", triangular_number_func(N))
