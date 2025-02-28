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
        lines = found.readlines()

        if(not lines):
            print("No files were found with that name! Returning to menu...")
            os.system("sleep 3")
            valid = False

        else:
            print("The following files were found:\n")
            
            for line in lines:
                print(f'[{index}] {line}')
                files_dict.update({index: line})
                index += 1

    os.system("rm tmp.txt")

    if(valid):
        exit_link = False

        while(not exit_link):
            link_choice = input("Enter the file you would like to make a symbolic link for: ")

            if(link_choice.isdigit()):
                test = files_dict.get(int(link_choice))

                if(test is not None):
                    print("Creating link... please wait")
                    os.system(f'ln -s {test.strip()} ~/Desktop')
                    os.system('echo "Link sucessfully created! Returning to menu..." && sleep 3')
                    exit_link = True
                
                else:
                    print("Invalid choice!\n")
            
            else:
                print("Invalid choice!\n")

def delete_link():
    os.system("clear")
    link = input("Enter the symbolic link you would like to remove: ")
    os.system(f'ls -la ~/Desktop | grep "{link} \->" > tmp.txt')

    with(open("tmp.txt", "r")) as links:
        lines = links.readlines()

        delete_dict = dict()
        index = 1

        if(lines):
            print("The following links were found:")

            for line in lines:
                print(f'[{index}] {line}')
                delete_dict.update({index: line})
                index += 1
        
        exit_link = False

        while(not exit_link):
            link_choice = input("Enter the link you would like to delete: ")

            if(link_choice.isdigit()):
                test = delete_dict.get(int(link_choice))

                if(test is not None):
                    print("Deleting link... please wait")
                    os.system(f'rm ~/Desktop/{link}')
                    os.system('echo "Link sucessfully deleted! Returning to menu..." && sleep 3')
                    exit_link = True
                
                else:
                    print("Invalid choice!\n")
            
            else:
                print("Invalid choice!\n")

        else:
            os.system('echo "The specified link does not exist! Returning to menu..." && sleep 3')

def link_report():
    os.system('clear && echo "Current active symbolic links on Desktop:\n"')
    os.system('sleep 1 && ls -la ~/Desktop | grep "\->" | awk \'{print $9}\' > tmp.txt')

    links_dict = dict()
    index = 1

    with(open("tmp.txt", "r")) as current_links:
        lines = current_links.readlines()

        if(not lines):
            print("No current links are active! Returning to menu...")
            os.system("sleep 3")
        
        else:
            print(str(len(lines)) + " links were found:\n")

            for line in lines:
                print(f'[{index}] {line}')
                links_dict.update({index: line})
                index += 1
        
    os.system("rm tmp.txt")

    return_choice = input("Press d to delete a link or any other key to return to the menu!")

    if(return_choice == "d"):
        delete_link()
    
    else:
        os.system('echo "Returning to menu..." && sleep 3')

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