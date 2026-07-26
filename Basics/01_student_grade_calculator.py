# ---------------------------------------------------------
# Program 1: Student Marks Calculator
# Concepts Used:
# Functions, Lists, Loops, Conditional Statements
# ---------------------------------------------------------

# ---------------------- Input ---------------------- #

student_name = input("Enter the student's name: ")

marks = []

print("\nEnter marks for 5 subjects:\n")

for i in range(1, 6):

    mark = int(input(f"Subject {i}: "))

    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()

    marks.append(mark)

# -------------------- Functions -------------------- #

# Calculate total marks
def total_marks(values):
    return sum(values)


# Calculate average marks
def average_marks(values):
    return sum(values) / len(values)


# Calculate grade based on average
def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "Fail"


# -------------------- Main Program -------------------- #

total = total_marks(marks)
average = average_marks(marks)
grade = calculate_grade(average)

print("\n" + "-" * 55)
print("             STUDENT MARKS CALCULATOR")
print("-" * 55)

print(f"\nStudent Name : {student_name}")

print("\nSubject Marks")
print("-" * 20)

for index, mark in enumerate(marks, start=1):
    print(f"Subject {index:<2} : {mark}")

print("\nResult")
print("-" * 20)

print(f"Total Marks     : {total}")
print(f"Average Marks   : {average:.2f}")
print(f"Final Grade     : {grade}")