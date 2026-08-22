# DataTypes in Python

# int - Integer
# Used for whole numbers, without decimal values.

age = 18
marks = 90
temperature = -5
low = 0

print(type(age))
print(type(marks))
print(type(temperature))
print(type(low))

# float - Decimal Number
# Used for numbers containing decimals values.

price = 99.99
percentage = 87.5
height = 5.8

print(type(price))
print(type(percentage))
print(type(height))

# str - String
# Used for text. 
# Strings are enclosed in quotes - Single or Double Quotes.

name = "Rozy"
city = 'Delhi'
message = "Hello World"

# Numbers inside quotes becomes string.

number = "100"

print(type(name))
print(type(city))
print(type(message))
print(type(number))

# bool - Boolean
# Boolean has only two values - True & False.

is_student = True
is_logged_in = False

is_student = type(is_student)
is_logged_in = type(is_logged_in)

# Boolean values are commonly produced by comparisons.

age = 18
print(age>=18)
print(age==18)
print(age<18)

# None - Represents intentional absense of value or a null value.

password = None

print(type(password))

# Comments - Part of code which compiler ignore during the execution of program.
# It is mainly used for explaining the code.

# There are two types of comments in python

# - Single-Line Comments

'''
    Multi-Line Comments
'''