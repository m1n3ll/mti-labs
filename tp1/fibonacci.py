# Procedural 

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 6
print("Fibonacci number (Procedural):", fibonacci(n))

# Functional

from functools import lru_cache

#@lru_cache makes the recursion more efficient (no repeated calculations).

@lru_cache(None)
def fibonacci_func(n):
    return 1 if n <= 1 else fibonacci_func(n - 1) + fibonacci_func(n - 2)

# Test
n = 6
print("Fibonacci number (Functional):", fibonacci_func(n))

