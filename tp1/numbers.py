
from functools import reduce 

#numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(): Apply a function to each element in the list

squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# filter(): Keep only the elements that meet a condition

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce(): Combine all elements into a single value

total_sum = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", total_sum)

# Combine them all together 
# lambda : small, one-line anonymous function

sum_of_even_squares = reduce(lambda a, b: a + b,
                             map(lambda x: x ** 2,
                                 filter(lambda x: x % 2 == 0, numbers)))
print("Sum of squares of even numbers:", sum_of_even_squares)
