try:
    student_name = input("Enter the student's name: ")

    marks = []

    # Input and validation
    for i in range(1, 6):
        mark = int(input(f"Enter marks for Subject {i}: "))

        if mark < 0 or mark > 100:
            print("Error: Marks should be between 0 and 100.")
            exit()

        marks.append(mark)

    # Calculate total and average
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    # Function to determine grade
    def calculate_grade(avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "Fail"

    grade = calculate_grade(average_marks)

    # Display Result
    print("\n---------- RESULT ----------")
    print(f"Student Name : {student_name}")

    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i} : {mark}")

    print(f"\nTotal Marks : {total_marks}")
    print(f"Average     : {average_marks:.2f}")
    print(f"Grade       : {grade}")

except ValueError:
    print("Error: Please enter valid numeric marks.")