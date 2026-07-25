# ---------------------------------------------------------
# Program 3: List Analyzer
# Concepts Used:
# Lists, Loops, Functions, Conditional Statements
# ---------------------------------------------------------

# ---------------------- Input ---------------------- #

numbers = []

print("Enter 10 integers:\n")

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# -------------------- Functions -------------------- #

# Find the largest number
def largest_number(values):
    return max(values)


# Find the smallest number
def smallest_number(values):
    return min(values)


# Find the second largest unique number
def second_largest(values):
    unique_numbers = list(set(values))

    if len(unique_numbers) < 2:
        return "Not Available"

    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)


# Calculate the sum of all numbers
def total_sum(values):
    return sum(values)


# Calculate the average
def average(values):
    return sum(values) / len(values)


# Find all even numbers
def even_numbers(values):
    even = []

    for number in values:
        if number % 2 == 0:
            even.append(number)

    return even


# Find all odd numbers
def odd_numbers(values):
    odd = []

    for number in values:
        if number % 2 != 0:
            odd.append(number)

    return odd


# -------------------- Main Program -------------------- #

print("\n" + "-" * 55)
print("                 LIST ANALYZER PROGRAM")
print("-" * 55)

print("\nList Values")
print("-" * 20)

for index, number in enumerate(numbers, start=1):
    print(f"{index}. {number}")

print("\nAnalysis")
print("-" * 20)

print(f"Largest Number        : {largest_number(numbers)}")
print(f"Smallest Number       : {smallest_number(numbers)}")
print(f"Second Largest Number : {second_largest(numbers)}")
print(f"Sum of Numbers        : {total_sum(numbers)}")
print(f"Average               : {average(numbers):.2f}")
print(f"Even Numbers          : {even_numbers(numbers)}")
print(f"Odd Numbers           : {odd_numbers(numbers)}")