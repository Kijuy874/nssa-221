#/bin/python3.9

import os

def menu():
    while(True):
        print("1. Display the default gateway")
        print("2. Test Local Connectivity")
        print("3. Test Remote Connectivity")
        print("4. Test DNS Resolution")
        print("5. Exit/quit the script")

        choice = input("Select an option (1-5): ")
        match choice:
            case 1:
                os.system("ip r | awk '{print $3}'")
            case 2:
                print("TODO")
            case 3:
                print("TODO")
            case 4:
                print("TODO")
            case 5:
                exit
            case _:
                print("Invalid choice")

def main():
    menu()

if "__name__" == "__main__":
    main()