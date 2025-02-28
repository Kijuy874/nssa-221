#!/bin/python3.9

import os

def create_link():
    os.system('clear')
    file = input("Enter the file name you would like to create a link for: ")
    os.system('find / -type f -name "' + file +'" 2>/dev/null')

def delete_link():
    print("TODO")

def link_report():
    print("TODO")

def menu():
    os.system("clear")
    os.system('echo "You are currently at: $(pwd)"')

    exit = False

    while(not exit):
        os.system("clear")
        print("Welcome to the Symbolic Link Shortcut!\n")

        print(" \
              [1] Create a symbolic link\n \
              [2] Delete a symbolic link\n \
              [3] Generate a symbolic link report\n \
              [4] Quit\n")
        
        choice = input("Select an option: ")

        # Perform logic based on user input
        if(choice == "1"):
            create_link()
        
        elif(choice == "2"):
            delete_link()

        elif(choice == "3"):
            link_report()

        elif(choice == "4"):
            print("\nGoodbye!")
            os.system("sleep 3 && clear")
            exit = True

        else:
            print("Invalid choice!")
            os.system("sleep 3")

menu()