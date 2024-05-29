import student_management
import utils

def add_student_marks():
    student_id = input("Enter student ID to add marks: ")
    if student_id in student_management.students:
        subject_name = input("Enter subject name: ")
        marks = input("Enter marks: ")
        if subject_name in student_management.students[student_id]['subject']:
            student_management.students[student_id]['subject'][subject_name]['marks'] = int(marks)
        else:
            fees = input("Enter fees: ")
            student_management.students[student_id]['subject'][subject_name] = {
                'marks': int(marks),
                'fees': int(fees)
            }
        utils.log_transaction(f"Added marks for student: {student_id}, subject: {subject_name}")
        print("Marks added successfully.")
    else:
        print("Student ID not found. Please try again.")

def view_own_students():
    for student_id, details in student_management.students.items():
        print(f"ID: {student_id}, Name: {details['fname']} {details['lname']}, Marks: {details['subject']}")
