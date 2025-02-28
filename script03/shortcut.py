#!/bin/python3.9

import os

def create_link():
    os.system('clear')
    file = input("Enter the file name you would like to create a link for: ")
    os.system('find / -type f -name "' + file +'" 2>/dev/null > tmp.txt')

    files_dict = dict()
    valid = True

    print("The following files were found:\n")
    with(open("tmp.txt", "r")) as found:
        index = 1
        for line in found:
            if(index == 1 and not line.strip()):
                print("No files were found with that name! Returning to menu...")
                valid = False
                break
            else:
                print(f"[{index}] {line}")
                files_dict.update({index: line})
                index += 1

    os.system("rm tmp.txt")

    if(valid):
        link_choice = input("Enter the file you would like to make a symbolic link for: ")
        print("Creating link... please wait")

        if(link_choice in files_dict.keys):
            os.system(f'ln -s {str(files_dict.get(str(link_choice))).strip()} ~/Desktop')
            print("Link sucessfully created! Returning to menu...")

def delete_link():
    print("TODO")

def link_report():
    print("TODO")

def menu():
    exit = False

    while(not exit):
        os.system("clear")
        os.system('echo "Welcome to the Symbolic Link Shortcut!"')
        os.system('echo "You are currently at: $(pwd)" && echo ""')
        
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
            os.system("sleep 3")
            exit = True

        else:
            print("Invalid choice!")
            os.system("sleep 3")

menu()