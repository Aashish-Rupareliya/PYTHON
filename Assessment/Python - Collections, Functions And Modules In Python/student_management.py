import utils

students = {}

def add_student():
    while True:
        student_id = input("Enter student ID: ")
        if student_id in students:
            print("Student ID already exists. Please try again.")
            continue
        
        first_name = input("Enter first name: ")
        if not first_name.isalpha():
            print("Invalid first name. Please enter only alphabetic characters.")
            continue
        
        last_name = input("Enter last name: ")
        contact_number = input("Enter contact number: ")
        if not contact_number.isdigit():
            print("Invalid contact number. Please enter only digits.")
            continue
        
        subjects = {}
        while True:
            subject_name = input("Enter subject name (or 'done' to finish): ")
            if subject_name.lower() == 'done':
                break
            marks = input(f"Enter marks for {subject_name}: ")
            fees = input(f"Enter fees for {subject_name}: ")
            subjects[subject_name] = {
                'marks': int(marks),
                'fees': int(fees)
            }
        
        faculty_name = input("Enter faculty name: ")
        
        students[student_id] = {
            'fname': first_name,
            'lname': last_name,
            'contact': contact_number,
            'subject': subjects,
            'faculty': faculty_name
        }
        utils.log_transaction(f"Added student: {student_id}")
        print("Student added successfully.")
        break

def remove_student():
    student_id = input("Enter student ID to remove: ")
    if student_id in students:
        confirm = input("Are you sure you want to delete this student? (Y/N): ")
        if confirm.lower() == 'y':
            del students[student_id]
            utils.log_transaction(f"Removed student: {student_id}")
            print("Student removed successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Student ID not found. Please try again.")

def view_all_students():
    if students:
        for student_id, details in students.items():
            print(f"{student_id}: {details}")
    else:
        print("No students found.")

def view_student():
    student_id = input("Enter student ID to view: ")
    if student_id in students:
        details = students[student_id]
        print(details)
    else:
        print("Student ID not found. Please try again.")
