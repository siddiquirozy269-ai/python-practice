# Revision Variables
# Variable Assignment
# '=' operator used for assigning a variable

name = 'Rozy' # String type variable
age = 18 # Integer type variable
marks = 87.5 # Float type variable
is_Student = True

# Multiple Variables in One Line

a, b, c, d = 10, 20, 30, 40

# a=10
# b=20
# c=30
# d=40

print(a)
print(b)
print(c)
print(d)

# Constants - values intended to remain unchanged
# Python uses UPPER_CASE as the naming convention for constants

PI=3.14
MAX_LIMIT=30

# Temporary Variables
# Used for swapping

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Delete Variables
# Syntax: del var_name

x = 23
del x
# x variable is deleted now

# Check Variable Type
# Function - type() 
# syntax : type(var_name)

student_id = 110234
student_name = "Rozy"
student_marks = 95.8

print(type(student_id))
print(type(student_name))
print(type(student_marks))

# Best Practices
# Snake Case Naming

user_age = 18
is_logged_in = False

# Valid Variables Names

student_name = "Jone"
age2 = 18
_user = "admin"
student_2026 = True

# Invalid Variable Names

# 2age = 18                     #Cannot start with a number
# student name = Jone           #Spaces are not allowed
# class = BCA                   #Keywords are not allowed because it is already reserved