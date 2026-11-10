
# grading_system.py
# Task 2: Build the application
# ICT111 - Student Grading System

students = []  # list of dictionaries


def get_grade_and_decision(mark):
    """Assign grade and decision using if/elif/else (Task 2.4)"""
    if mark >= 80:
        return "A", "Excellent"
    elif mark >= 70:
        return "B", "Very good"
    elif mark >= 60:
        return "C", "Good"
    elif mark >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


def add_student():
    """Add a student with full validation (Task 2.2 & 2.3)"""
    # Validate student number – reject blank
    while True:
        student_number = input("Enter student number: ").strip()
        if student_number:
            break
        print("Student number cannot be blank. Please try again.")

    # Validate name – reject blank
    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Name cannot be blank. Please try again.")

    # Validate mark – must be numeric and between 0–100
    while True:
        mark_input = input("Enter mark (0-100): ").strip()
        try:
            mark = float(mark_input)
            if 0 <= mark <= 100:
                break
            else:
                print("Mark must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Mark must be a number. Please try again.")

    # Assign grade and decision
    grade, decision = get_grade_and_decision(mark)

    # Store as dictionary inside the students list
    record = {
        "student_number": student_number,
        "name": name,
        "mark": mark,
        "grade": grade,
        "decision": decision
    }
    students.append(record)

    # Clear feedback after adding (Task 2.4)
    print(f"\nRecord added successfully!")
    print(f"  {student_number} | {name} | Mark: {mark} | Grade: {grade} | {decision}\n")


def display_all():
    """Display all records using a for loop (Task 2.5)"""
    if not students:
        print("\nNo student records found. Please add students first.\n")
        return

    print("\n" + "=" * 70)
    print(f"{'Student No.':<15} {'Name':<20} {'Mark':>8} {'Grade':>8} {'Decision':<12}")
    print("-" * 70)
    for student in students:
        print(f"{student['student_number']:<15} "
              f"{student['name']:<20} "
              f"{student['mark']:>8.1f} "
              f"{student['grade']:>8} "
              f"{student['decision']:<12}")
    print("=" * 70 + "\n")


def main():
    """Main menu using while loop (Task 2.1)"""
    print("=" * 50)
    print("   STUDENT GRADING SYSTEM")
    print("   Mulungushi University - ICT111")
    print("=" * 50)

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Display all")
        print("3. Class summary")
        print("4. Exit")

        option = input("Choose 1-4: ").strip()

        if option == "1":
            add_student()
        elif option == "2":
            display_all()
        elif option == "3":
            # Placeholder for Task 3 – you can add class_summary() later
            print("\nClass summary will be implemented in Task 3.\n")
        elif option == "4":
            print("\nThank you for using the Student Grading System. Goodbye!")
            break
        else:
            print("\nInvalid option. Please choose a number between 1 and 4.\n")


if __name__ == "__main__":
    main()










