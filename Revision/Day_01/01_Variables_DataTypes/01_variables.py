# Data Types in Python

# --------------------------------------------------
# 1. int - Integer
# Used for whole numbers without decimal values.
# --------------------------------------------------

age = 18
marks = 90
temperature = -5
low = 0

print(type(age))
print(type(marks))
print(type(temperature))
print(type(low))


# --------------------------------------------------
# 2. float - Floating Point Number
# Used for numbers containing decimal values.
# --------------------------------------------------

price = 99.99
percentage = 87.5
height = 5.8

print(type(price))
print(type(percentage))
print(type(height))


# --------------------------------------------------
# 3. str - String
# Used for text.
# Strings can be enclosed in single or double quotes.
# --------------------------------------------------

name = "Rozy"
city = 'Delhi'
message = "Hello World"

# Numbers inside quotes become strings.

number = "100"

print(type(name))
print(type(city))
print(type(message))
print(type(number))


# --------------------------------------------------
# 4. bool - Boolean
# Boolean has only two values: True and False.
# --------------------------------------------------

is_student = True
is_logged_in = False

print(type(is_student))
print(type(is_logged_in))


# Boolean values are commonly produced by comparisons.

age = 18

print(age >= 18)
print(age == 18)
print(age < 18)


# --------------------------------------------------
# 5. None
# Represents the intentional absence of a value.
# --------------------------------------------------

password = None

print(type(password))


# --------------------------------------------------
# 6. Comments
# Comments are text in the code that Python ignores
# during execution. They are mainly used to explain code.
#
# Single-Line Comment:
# This is a single-line comment.

# Multi-Line String:
"""
This is a multi-line string.
It can span across multiple lines.
"""