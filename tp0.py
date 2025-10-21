#Task 1
print("Hello, World !")
name = "Manel" # used a string for name
age = 21 # used an int for the age
job = "jobless" # used another string for the job
weight = 56 # used int for the weight
height = 1.60 # didnt have to declare it as a float since python can understand itself

print ("My name is ", name)
print("I'm", age, " years old")
print("I'm", job)
print("My weight is ", weight, "kg")
print("I'm also", height, "cm")

name = input("Enter your name :")
age = input("How old are you ?")
job = input("What do you do for a living ?")
weight = input("How much do you weight ?")
height = input("How tall are you? ")

#Task 2
Prod_cod = input("Enter your product code :")
Prod_name = input("Enter you product name :")
Unit_price = float(input("Enter the price :"))
Prod_quantity = int(input("Enter the quantity :"))
Prod_stock = input("Enter how much there's in the stock :")
Tax_rate = input("Enter your tax rate :")

Prod_stock = float(Prod_stock)
Tax_rate = float(Tax_rate)

subtotal = Prod_quantity * Unit_price
tax_amount = subtotal * Tax_rate
total_cost = subtotal + tax_amount
new_stock = Prod_stock - Prod_quantity


receipt = f"""
******************************* ORDER RECEIPT *******************************
Product Code:   {Prod_cod}
Item:           {Prod_name}
Price/Unit:     {Unit_price:.2f} DA
Quantity:       {Prod_quantity}
Stock:          {Prod_stock:.0f}

Subtotal:       {subtotal:.2f} DA
Tax ({Tax_rate * 100:.2f}%):  {tax_amount:.2f} DA
******************** Total Cost: {total_cost:.2f} DA
******************** Remaining Stock: {new_stock:.0f}
***************************************************************************
"""

# f before quotes tell python to replace whats inside {} with their values
# """ allows the text to span multiple lines like paragraphs
# :.2 means shows 2 digits after the decimal point, f is for the floating point number, and the : to start a format
print(receipt)

#Task 3
number = input("Enter a number :")
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

year = input("Enter a year :")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
# % is for modulo

#Task 4
grade = float(input("Enter your score (0-100): "))
if 90 <= grade <= 100:
    print("Your grade is: A")
elif 80 <= grade < 90:
    print("Your grade is: B")
elif 70 <= grade < 80:
    print("Your grade is: C")
elif 60 <= grade < 70:
    print("Your grade is: D")
else:
    print("Your grade is: F")
 
 
 
day_number = int(input("Enter a day number (1-7): "))
if day_number == 1:
    print("Saturday")
elif day_number == 2:
    print("Sunday")
elif day_number == 3:
    print("Monday")
elif day_number == 4:
    print("Tuesday")
elif day_number == 5:
    print("Wednesday")
elif day_number == 6:
    print("Thursday")
elif day_number == 7:
    print("Friday")
else:
    print("Invalid number! Please enter between 1 and 7.")

#Task 5
for i in range(9):
 print( "9 x ", i, "  = ", 9*i)

#Task 6
total = 0
count = 0
i = int(input("Enter a number : "))

while i != 0:
    total += i
    count += 1
    i = int(input("Enter a number : "))

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers were entered.")


#Task 7

for i in range(1, 21):
    if i % 3 == 0:
        continue   #skips multiples of 3
    print(i)

#Task 8

Names = ["Nermin", "Riadh", "Youcef", "Manel", "Wafa"]
for name in Names:
 print(name)

#Task 9

Fruits = ["apple", "banana", "cherry", "date", "orange", "mango", "pears"]

print("Full list of fruits:", Fruits)
 
print(Fruits[0])
print(Fruits[-1])
print(Fruits[4])
print(Fruits[0])
print(Fruits[10])

#Task 10

small_numbers = [10, 20, 30, 40, 50]
print(small_numbers)
small_numbers[1]= 25
print(small_numbers)
small_numbers.append(60)
print(small_numbers)
small_numbers.insert(0, 5)
print(small_numbers)
small_numbers.remove(30)
print(small_numbers)

large_numbers = [100, 200, 300, 400, 500]
print(large_numbers)
combined_list = small_numbers + large_numbers
print(combined_list)

present = 30 in combined_list
print(present)
print(len(combined_list))
combined_list.sort(reverse=True)
print(combined_list)

#Task 11

temperatures = [22.5, 24.1, 23.8, 25.0, 21.9]
for temp in temperatures:
    print(temp)
max_temp = max(temperatures)
print(max_temp)
average_temp = sum(temperatures) / len(temperatures)
print(average_temp)

#Task 12

student_scores = [85, 92, 78, 95, 88]
search = int(input("Enter a score to search for:"))
if search in student_scores:
    index = student_scores.index(search)
    print(f"Score {search} found at index {index}")
else:
    print("Score not found")

student_scores[2]= 80
print(student_scores)

#Task 13


data_points = [10, 15, 20, 25, 30, 35]
total = sum(data_points)
print(total)

count = 0
for point in data_points:
    if point > 20:
        count += 1

print(count)

#Task 14

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(matrix[0][1])
print(matrix[2][2])

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  
    
#Task 15


a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]

result_matrix = [
    [0, 0],
    [0, 0]
]

for i in range(len(a)):            # loop through rows
    for j in range(len(a[0])):     # loop through columns
        result_matrix[i][j] = a[i][j] + b[i][j]

for row in result_matrix:
    print(row)
    

#Task 16

coordinates = (10.5, 20.3)
print(coordinates)

print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])

person_info = ("Alice", 30, "New York")
name, age, city = person_info
print("Name:", name)
print("Age:", age)
print("City:", city)

def get_min_max(numbers):
    return (min(numbers), max(numbers))

result = get_min_max([5, 1, 9, 2, 7])
print("Min and Max values:", result)

students = [("Bob", 85), ("Charlie", 92), ("David", 78)]
for name, score in students:
    print(f"{name} scored {score}")
    

#Task 17


student_profile = {
    "name": "Eve",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student_profile)
print("Name:", student_profile["name"])
print("Major:", student_profile["major"])

student_profile["university"] = "Tech University"
student_profile["gpa"] = 3.9
del student_profile["age"]

print("\nUpdated Student Profile:", student_profile)



print("\nKeys:")
for key in student_profile.keys():
    print(key)


print("\nValues:")
for value in student_profile.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student_profile.items():
    print(f"{key}: {value}")
    


library = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925},
    "1984": {"author": "George Orwell", "year": 1949}
}

print("\nAuthor of '1984':", library["1984"]["author"])


library["To Kill a Mockingbird"] = {"author": "Harper Lee", "year": 1960}


print("\nLibrary Books and Authors:")
for title, info in library.items():
    print(f"{title} — Author: {info['author']}")
