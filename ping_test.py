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

        if(choice == 1):
            os.system("ip r | awk '{print $3}'")
        elif(choice == 2):
            print("TODO")
        elif(choice == 3):
            print("TODO")
        elif(choice == 4):
            print("TODO")
        elif(choice == 5):
            print("TODO")
        else:
            print("Invailid choice")

def main():
    menu()

if "__name__" == "__main__":
    main()