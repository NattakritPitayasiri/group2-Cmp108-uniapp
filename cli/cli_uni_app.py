def university_menu():
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").upper()

        if choice == "A":
            input("  Admin System (c/g/p/r/s/x):")
        elif choice == "S":
            input("  Student System (l/r/x):")
        elif choice == "X":
            print("Thank You")
            return
        else:
            print("Please select your Account Type")





if __name__ == "__main__":
    main()

    