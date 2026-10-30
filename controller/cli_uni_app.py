import controller.student_system
from controller.admin_system import AdminSystem
from model.database import Database

def admin_menu():
    database = Database()
    admin = AdminSystem(database)
    admin.admin_subsystem()


def student_menu():
    while True:
        student_action = input("  Student System (l/r/x):").lower()
        if student_action == "x":
            break
        elif student_action == "r":
            print("Student Sign Up")
            controller.student_system.register()
        elif student_action == "l":
            print("Student Sign In")
            controller.student_system.login()
        else:
            print("Invalid choice. Please try again")
        

def main(): ## Neo Only
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").upper()
        if choice == "A":
            admin_menu()
        elif choice == "S":
            student_menu()
        elif choice == "X":
            print("Thank You")
            break
        else:
            print("Please select your Account Type")


if __name__ == "__main__":
    main()

