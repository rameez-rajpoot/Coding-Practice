# Output

# print("Hello World!")
# print("Rameez Rajpoot")

# Variable

# name = 'Rameez Rajpoot'
# age = 19
# print(name,age)
# print(type(name),type(age))

# input
# name = input("Enter your name: ")
# print(name)

# Practice 
# first_name = 'Tony'
# last_name = 'Stark'
# tony_age = 35
# tony_height = 1.85

# name = input()
# print(name,type(name)) #  By default input is string
# print("Tony is secretly a:",name)

# Type conversion & Type Casting

# a = 1 + 2.5     # Implicit
# print(a)
# a = 1 + int(2.5)    # Explicit
# print(a)

# Sum program

# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# print("Sum of a & b is:",a+b)

# String Operations

# name = "Rameez Rajpoot"
# print(name.upper())
# print(name.lower())
# print(name)     # Deep Copy means no change in original data
# print(name.find('Raj'))
# print(name.replace("Rajpoot","Shahid"))
# print('Ra' in name)

# Practice

# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

# total_bill = (a+b+c)
# average_bill = (a+b+c)/3

# print("Total bill:",total_bill)
# print("Average bill:",average_bill)

# name = input()
# print('S' in name)
# print('s' in name)

# Arithematic Operators
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

# Assignment Operators
# x = 3
# x += 3
# print(x)
# x -= 1
# print(x)
# x *= 2
# print(x)
# x /= 2
# print(x)
# x %= 2
# print(x)

# Comparison Operators
# <, <=, >, >=, ==, !=

# print(5 > 2)
# print(5 >= 2)
# print(5 < 2)
# print(5 <= 2)
# print(5 == 2)
# print(5 != 2)

# Logical Operators
# && (and), || (or), ! (not)

# print((3>2) and (1>10))
# print((3>2) or (1>10))
# print(not (1>10))

# Coditional if

# marks = int(input("Enter marks: "))

# if marks >= 80 or marks <= 100:
#   print('A')
# elif marks >= 60 or marks <= 80:
#   print('B')
# else:
#   print('C')

# Project of Calculator
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# o = input("Enter the operation: ")

# if o == '+':
#   print("Sum of",a,"and",b,":",a+b)
# elif o == '-':
#   print("Difference of",a,"and",b,":",a-b)
# elif o == '/':
#   print("Division of",a,"and",b,":",a/b)
# elif o == '*':
#   print("Product of",a,"and",b,":",a*b)
# elif o == '%':
#   print("Remainder of",a,"and",b,":",a%b)
# elif o == '**':
#   print("Value of Power of",a,"to",b,":",a**b)
# else:
#   print("You entered invalid operator")
  
# print("Thank you for using calculator")

# Loops
# While loop

# i = 1
# while i <= 5:
#     print(i * "*")
#     i +=1
    
# print("Loop ends")
    
# For loop

# num = range(11)
# for i in num:
#     print(i)
    
# for i in range(11):
#     print(i)
    
# print even numbers

# for i in range(2,11):
#     if i % 2 == 0:
#         print(i)
        

# for i in range(2, 11, 2):
#     print(i)

# Print multiples of 3 upto 51
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)

# But if we want to stop the loop the in any certain point like after 21 then we use break statement

# for i in range(1, 51):
#     if i == 21:
#         break
#     if i % 3 == 0:
#         print(i)
        
# But if we want to skip the loop in any certain point or value like we want to skip the value 21 then we use continue statement

# for i in range(1, 51):
#     if i == 21:
#         continue
#     if i % 3 == 0:
#         print(i)

# Practice Exercise

# Print all odd num b/w 1 to 20
# for i in range(1, 20):
#     if i % 2 ==1:
#         print(i)

# Print the table of 57
# num = 57
# for i in range(1, 11):
#     print("",num,"*",i,"=",num*i)

# Print all multiple of 3 from 1 to 50 but skip 15
# for i in range(1, 51):
#     if i == 15:
#         continue
#     if i % 3 == 0:
#         print(i)

# Take two integers a and b as input
# Find and print 1st num b/w 1 to 1000 that is divisible by both a and b.

# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# for i in range(1, 1001):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
# else:
#     print("Can't find the number")

# Studing about complex datatypes in Python
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# Studing about list and its operations Python Programming
# List are mutable means they are modify or change once they created

# marks = [98, 94, 91, 90, 70, 75]
# print(marks, type(marks))
# for score in marks:
#     print(score)
# print(marks.count(98))
# print(marks.index(98))

# Operations on list
# Find length of list
# print(len(marks))
# Find any index value
# print(marks[5])
# Add any value to the last
# marks.append(99)
# print(marks)
# Insert any value to the list
# marks.insert(2, 100)
# print(marks)
# Slicing taking a part of list as output
# print(marks[0:5])

# print(marks[-4:-1])

# Find any value from the list
# print(90 in marks)
# Clear the list
# marks.clear()
# print(marks)

# Learning about Tuples in Python Programming
# Tuples are Immutable means they can't modify or change once they created
# If you want then remove the paranthesis they are not compulsory

# marks = (98, 94, 91, 90, 70, 75)
# for score in marks:
#     print(score)
# print(marks, type(marks))
# print(marks.count(98))
# print(marks.index(98))

# Operations on tuple
# Find length of tuple
# print(len(marks))
# Find any index value
# print(marks[5])
# Slicing taking a part of tuple as output
# print(marks[0:5])

# print(marks[-4:-1])

# Find any value from the tuple
# print(90 in marks)


# Learning about Set in Python Programming
# Unique items collection
# marks = {98, 75, 70, 90, 70, 75}
# print(marks)
# print(len(marks), type(marks))

# for score in marks:
#     print(score)

# Operations on tuple
# Find length of tuple
# print(len(marks))

# Find any value from the tuple
# print(90 in marks)

# Learning about Dictionary in Python Programming
# Dictionary word => meaning
# Dictionary key => value (Dictionary is key value pair type)

# marks = {"Math":99, "Physics":90, "Computer":75}
# print(marks, type(marks))

# marks["English"] = 90

# print(marks)

# for key in marks:
#     print(key, marks[key])

# Practice Exercise
# A list of roll no. and print all unique roll no.

# roll_no = [101, 102, 103, 101, 105, 106]
# roll_no = set(roll_no)
# print(roll_no)

# Add a list of tuples enter employee id and find it in the list of tuples
# employee = [
#     (101, "Alice", 65000),
#     (102, "Bob", 50000),
#     (103, "Charlie", 45000)
# ]

# emp_id = int(input("Enter employee id : "))

# for emp in employee:
#     if emp[0] == emp_id:
#         print("Employee found!")
#         print("Employee id is :",emp[0])
#         print("Employee name is :",emp[1])
#         print("Employee salary is :",emp[2])
#         break
# else:
#     print("Employee not found !!!")

# Learning about Functions in Python Programming
# def sum(a, b):
#     print(a+b)
    
# sum(111,444)

# def calc_gst(price):
#     new_price = price + price*0.18
#     return new_price
    
# print(calc_gst(200))

