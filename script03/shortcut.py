#!/bin/python3.9

import os

def create_link():
    os.system('clear')
    file = input("Enter the file name you would like to create a link for: ")
    os.system('find / -type f -name "' + file +'" 2>/dev/null > tmp.txt')

    files_dict = dict()
    valid = True
    index = 1

    with(open("tmp.txt", "r")) as found:
        if(not found.readlines()):
            print("No files were found with that name! Returning to menu...")
            os.system("sleep 3")
            valid = False

        else:
            print("The following files were found:\n")
            
            for line in found:
                print(f'[{index}] {line}')
                files_dict.update({index: line})
                index += 1

    os.system("rm tmp.txt")

    if(valid):
        exit_link = False

        while(not exit_link):
            link_choice = input("Enter the file you would like to make a symbolic link for: ")

            if(link_choice.isdigit()):
                test = files_dict.get(int(link_choice)).strip()

                if(test is not None):
                    print("Creating link... please wait")
                    os.system(f'ln -s {test} ~/Desktop')
                    print("Link sucessfully created! Returning to menu...")
                    exit_link = True
                
                else:
                    print("Invalid choice!\n")
            
            else:
                print("Invalid choice!")

def delete_link():
    print("TODO")

def link_report():
    print("Current active symbolic links on Desktop:\n")
    os.system('ls -la ~/Desktop | grep "\->" | awk \'{print $9}\' > tmp.txt')

    links_dict = dict()
    valid = True
    index = 1

    with(open("tmp.txt", "r")) as current_links:
        if(not current_links.readlines()):
            print("No current links are active! Returning to menu...")
            os.system("sleep 3")
            valid = False
        
        else:
            print("The following links were found:\n")

            for line in current_links:
                print(f'[{index}] {line}')
                links_dict.update({index: line})
                index += 1

    if(valid):
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

        elif(choice == "4" or choice == "exit" or choice == "quit"):
            print("\nGoodbye!")
            os.system("sleep 3")
            exit = True

        else:
            print("Invalid choice!")
            os.system("sleep 3 && clear")

menu()