from student_management import (
    add_student, 
    remove_student, 
    view_all_students, 
    view_student
)
from faculty_management import add_student_marks, view_own_students

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Counsellor Menu")
        print("2. Faculty Menu")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            counsellor_menu()
        elif choice == '2':
            faculty_menu()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def counsellor_menu():
    while True:
        print("\nCounsellor Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. View Specific Student")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            view_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def faculty_menu():
    while True:
        print("\nFaculty Menu:")
        print("1. Add Student Marks")
        print("2. View Own Students")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student_marks()
        elif choice == '2':
            view_own_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
