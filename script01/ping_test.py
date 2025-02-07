#/bin/python3.9

# Tri Tran - Friday, February 7, 2025

import os

# Retrieves the default gateway of the system
def display_default_gateway():
    os.system("clear")
    print("\nThe default gateway is: ", end="")
    os.system("ip r | head -1 | awk '{print $3}' && sleep 3")

# Pings the default gateway and notifies user if test is successful or not
def test_local_connectivity():
    os.system("clear")
    print("\nPinging the default gateway")
    os.system("ping -c 4 $(ip r | head -1 | awk '{print $3}') | awk '/received/ {print $6}' > tmp.txt")
    packet_loss = open("tmp.txt", "r")
    
    if(packet_loss.read().strip() == "0%"):
        print("Please let your system administrator know the test was SUCCESSFUL")
    else:
        print("Please let your system administrator know the test has FAILED")
    
    os.system("rm tmp.txt && sleep 3")

# Pings RIT's DNS Server and notifies user if test is successful or not
# Totally following the DRY principle here :wink:
def test_remote_connectivity():
    os.system("clear")
    print("\nPinging remote address 129.21.3.17")
    os.system("ping -c 4 129.21.3.17 | awk '/received/ {print $6}' > tmp.txt")
    packet_loss = open("tmp.txt", "r")
    
    if(packet_loss.read().strip() == "0%"):
        print("Please let your system administrator know the test was SUCCESSFUL")
    else:
        print("Please let your system administrator know the test has FAILED")
    
    os.system("rm tmp.txt && sleep 3")

# Attempts to resolve Google to an IP and notifies user of the result
def test_dns_resolution():
    os.system("clear")
    print("\nTesting the DNS resolution for www.google.com")
    os.system("nslookup www.google.com | awk '/NXDOMAIN/' > tmp.txt")
    dns_result = open("tmp.txt", "r")

    if(dns_result.read().strip() == ""):
        print("Please let your system administrator know the test was SUCCESSFUL")
    else:
        print("Please let your system administrator know the test has FAILED")

    os.system("rm tmp.txt && sleep 3")

def menu():
    # Continually loop until user exits
    while(True):
        os.system("clear")
        print("Welcome to Ping Test!\n")

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
            display_default_gateway()
        
        elif(choice == "2"):
            test_local_connectivity()

        elif(choice == "3"):
            test_remote_connectivity()

        elif(choice == "4"):
            test_dns_resolution()

        elif(choice == "5"):
            print("\nGoodbye!")
            os.system("sleep 3 && clear")
            break

        # Prevent unintended input from executing
        else:
            print("Invailid choice")
            os.system("sleep 3")

# Program entry point
menu()
exit