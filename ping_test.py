#/bin/python3.9

# Tri Tran - Friday, February 7, 2025

import os

def menu():
    # Continually loop until user exits
    while(True):
        # Choices
        print("1. Display the default gateway")
        print("2. Test Local Connectivity")
        print("3. Test Remote Connectivity")
        print("4. Test DNS Resolution")
        print("5. Exit/quit the script")

        # Prompt user for menu option
        choice = input("Select an option (1-5): ")

        # Perform logic based on user input
        if(choice == "1"):
            os.system("ip r | head -1 | awk '{print $3}'")
        elif(choice == "2"):
            print("TODO")
        elif(choice == "3"):
            print("TODO")
        elif(choice == "4"):
            print("TODO")
        elif(choice == "5"):
            print("TODO")
        # Prevent unintended input from executing
        else:
            print("Invailid choice")

def main():
    # Clears the terminal before displaying the menu
    os.system("clear")
    menu()

# Good 'ol safeguarding if there was a test module
if "__name__" == "__main__":
    main()