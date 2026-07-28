# -----------------------------------------
# Student Management System
# Concepts: Lists, Dictionaries, Functions
# -----------------------------------------

student_details = [
    {"Roll No.": 1001, "Student Name": "Rozy", "Age": 18, "Marks": 95},
    {"Roll No.": 1002, "Student Name": "Shalu", "Age": 18, "Marks": 85},
    {"Roll No.": 1003, "Student Name": "Alisha", "Age": 19, "Marks": 91},
    {"Roll No.": 1004, "Student Name": "Rashid", "Age": 20, "Marks": 75},
    {"Roll No.": 1005, "Student Name": "Saif", "Age": 19, "Marks": 57}
]


# Add a new student
def add_student():
    roll_no = int(input("Enter Roll Number: "))
    student_name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

    duplicate = False

    # Check duplicate Roll Number
    for student in student_details:
        if student["Roll No."] == roll_no:
            duplicate = True
            break

    if duplicate:
        print("\nDuplicate Roll Numbers are not allowed!")
    else:
        new_record = {
            "Roll No.": roll_no,
            "Student Name": student_name,
            "Age": age,
            "Marks": marks
        }

        student_details.append(new_record)
        print("\nStudent Record Added Successfully!")


# View all students
def view_students():

    if len(student_details) == 0:
        print("\nNo Student Records Available.")
        return

    print("\n" + "-" * 45)

    for student in student_details:
        print(f"Roll No.      : {student['Roll No.']}")
        print(f"Student Name  : {student['Student Name']}")
        print(f"Age           : {student['Age']}")
        print(f"Marks         : {student['Marks']}")
        print("-" * 45)


# Search a student
def search_student():

    roll_no = int(input("Enter Roll Number: "))

    for student in student_details:
        if student["Roll No."] == roll_no:

            print("\nStudent Found")
            print("-" * 30)
            print(f"Roll No.      : {student['Roll No.']}")
            print(f"Student Name  : {student['Student Name']}")
            print(f"Age           : {student['Age']}")
            print(f"Marks         : {student['Marks']}")
            return

    print("\nStudent Record Not Found!")


# Update a student
def update_student():

    roll_no = int(input("Enter Roll Number to Update: "))

    for student in student_details:

        if student["Roll No."] == roll_no:

            student["Student Name"] = input("Enter New Student Name: ")
            student["Age"] = int(input("Enter New Age: "))
            student["Marks"] = int(input("Enter New Marks: "))

            print("\nStudent Record Updated Successfully!")
            return

    print("\nStudent Record Not Found!")


# Delete a student
def delete_student():

    roll_no = int(input("Enter Roll Number to Delete: "))

    for student in student_details:

        if student["Roll No."] == roll_no:

            student_details.remove(student)

            print("\nStudent Record Deleted Successfully!")
            print("-" * 30)
            print(f"Roll No.      : {student['Roll No.']}")
            print(f"Student Name  : {student['Student Name']}")
            print(f"Age           : {student['Age']}")
            print(f"Marks         : {student['Marks']}")
            return

    print("\nStudent Record Not Found!")


# -------------------------
# Main Menu
# -------------------------

while True:

    print("\n" + "=" * 50)
    print("         STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 50)

    try:

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("\nThank You! 💕")
            break

        else:
            print("\nPlease enter a valid choice (1-6).")

    except ValueError:
        print("\nError: Please enter a valid integer.")