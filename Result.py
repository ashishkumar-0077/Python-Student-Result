student = {}

while True:
    print("\-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice:")


    # Add Student
    if choice == "1":
        name = input("Enter student name:")
        marks = int(input("Enter student marks:"))
        student[name] = marks
        print("Student added successfully!")

    # View Student
    elif choice == "2":
        if not student:
            print("No Student Found!")
        else:
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")
    
    # Check Result
    elif choice == "3":
        name = input("Enter student name:")
        if name in student:
            marks = student[name]
            if marks >= 50:
                print(f"{name} has passed with marks: {marks}")
            else:
                print(f"{name} has failed with marks: {marks}")
        else:
            print("Student not found!")

    # Exit
    elif choice == "4":
        print("Exiting the application. Goodbye!")
        break
    else:        print("Invalid choice! Please try again.")