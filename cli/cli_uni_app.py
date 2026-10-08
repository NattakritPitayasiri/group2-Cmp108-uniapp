def main():
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").upper()

        if choice == "A":
            selected = input("  Admin System (c/g/p/r/s/x):")
        elif choice == "S":
            selected = input("  Student System (l/r/x):")
        elif choice == "X":
            print("Thank You")
            break
        else:
            print("Please select your Account Type")


if __name__ == "__main__":
    main()

    