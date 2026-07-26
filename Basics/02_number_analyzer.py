# ---------------------------------------------------------
# Program 2: Number Analyzer
# Concepts Used:
# Functions, Loops, Conditional Statements, Operators
# ---------------------------------------------------------

# ---------------------- Input ---------------------- #

number = int(input("Enter a number to analyze: "))

# -------------------- Functions -------------------- #

# Check whether the number is positive, negative, or zero
def check_sign(value):
    if value > 0:
        return "Positive"
    elif value < 0:
        return "Negative"
    else:
        return "Zero"


# Check whether the number is even or odd
def check_even_odd(value):
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Check whether the number is prime
def check_prime(value):

    if value <= 1:
        return False

    for i in range(2, value):
        if value % i == 0:
            return False

    return True


# Check whether the number is an Armstrong number
def check_armstrong(value):

    if value < 0:
        return False

    digits = len(str(value))
    temp = value
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == value


# Check whether the number is a palindrome
def check_palindrome(value):

    original = abs(value)
    temp = original
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    return reverse == original


# -------------------- Main Program -------------------- #

print("\n" + "-" * 55)
print("                NUMBER ANALYZER PROGRAM")
print("-" * 55)

print(f"\nEntered Number : {number}")

print("\nAnalysis")
print("-" * 20)

print(f"Number Type        : {check_sign(number)}")
print(f"Even / Odd         : {check_even_odd(number)}")

if check_prime(number):
    print("Prime Number       : Yes")
else:
    print("Prime Number       : No")

if check_armstrong(number):
    print("Armstrong Number   : Yes")
else:
    print("Armstrong Number   : No")

if check_palindrome(number):
    print("Palindrome Number  : Yes")
else:
    print("Palindrome Number  : No")