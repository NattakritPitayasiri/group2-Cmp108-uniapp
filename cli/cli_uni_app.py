def admin_menu():
    while True:
        admin_action = input("  Admin System (c/g/p/r/s/x):").lower()
        if admin_action == "x":
            break
        else:
            print("TBC") ##TBC Yinou

def student_menu():
    while True:
        student_action = input("  Student System (l/r/x):").lower()
        if student_action == "x":
            break
        else:
            print("TBC") ##TBC Jeongin
        

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

