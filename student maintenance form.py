# Initialize an empty list to store student records
students = []

# Function to accept student data
def accept_student():
    while True:
        name = input("Enter student name (or 'done' to exit): ")
        if name.lower() == 'done':
            break
        roll_no = input("Enter student roll number: ")
        marks = {
            "Engineering mathematics": float(input("Enter Engineering mathematics marks: ")),
            "Mechanincal engineering": float(input("Enter Mechanincal engineering marks: ")),
            "Human values": float(input("Enter Human values marks: "))
        }
        student_data = {"Name": name, "Roll Number": roll_no, "Marks": marks}
        students.append(student_data)
        print("Student data added successfully!")

# Function to display all student details
def display_students():
    if not students:
        print("No student records available.")
    else:
        print("Student Details:")
        for i, student in enumerate(students, 1):
            print(f"Student {i}:")
            for key, value in student.items():
                if key == "Marks":
                    print(f"  {key}:")
                    for subject, marks in value.items():
                        print(f"    {subject}: {marks}")
                else:
                    print(f"  {key}: {value}")
            print()

# Function to delete a student record
def delete_student(roll_no):
    for student in students:
        if student["Roll Number"] == roll_no:
            students.remove(student)
            print(f"Student with Roll Number {roll_no} deleted.")
            return
    print(f"Student with Roll Number {roll_no} not found.")

# Function to search for a student by roll number
def search_student(roll_no):
    for student in students:
        if student["Roll Number"] == roll_no:
            print("Student Details:")
            for key, value in student.items():
                if key == "Marks":
                    print(f"  {key}:")
                    for subject, marks in value.items():
                        print(f"    {subject}: {marks}")
                else:
                    print(f"  {key}: {value}")
            return
    print(f"Student with Roll Number {roll_no} not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Accept Student Data")
    print("2. Display Student Data")
    print("3. Delete Student Data")
    print("4. Search for a Student")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        accept_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        roll_no = input("Enter Roll Number of student to delete: ")
        delete_student(roll_no)
    elif choice == "4":
        roll_no = input("Enter Roll Number of student to search: ")
        search_student(roll_no)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
