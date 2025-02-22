#!/bin/python3.9

###
#   Tri Tran
#   NSSA-221.03
#   Friday, February 21, 2024
###

# Note: When using print() and os.system(), the command output was coming before print statements
# So everything is done using echo

import os
import platform

tabs = "\t\t\t\t" # Define standard tabbing across entire report

# Identify hostname and domain
def device_info():
    print("\nDevice Information")
    os.system(f'echo "Hostname:{tabs}$(hostname -s)"')
    os.system(f'echo "Domain:{tabs}\t$(domainname)"')


# Identify IP address, gateway, network mask, primary/secondary DNS
def network_info():
    print("\nNetwork Information")
    os.system(f'echo "IP Address:{tabs}$(hostname -I)"')
    os.system(f'echo "Gateway:{tabs}$(ip route show 0.0.0.0/0 | awk \'{{print $3}}\')"')
    os.system(f'echo "Network Mask:{tabs}$(route | awk \'$2 == \"0.0.0.0\" {{print $3}}\')"')
    os.system(f'echo "DNS1:{tabs}\t$(cat /etc/resolv.conf | awk \'$1 == \"nameserver\" {{print $2; exit}}\')"')
    os.system(f'echo "DNS1:{tabs}\t$(cat /etc/resolv.conf | awk \'$1 == \"nameserver\" {{count++; if (count == 2) print $2}}\')"')

# Identify operating system/version and kernel version
def os_info():
    print("\nOperating System Information")
    os.system('cat /etc/os-release | cut -d\'=\' -f2 | tr -d \'=\' | head -1 > tmp.txt')
    os.system('cat /etc/os-release | cut -d\'=\' -f2 | tr -d \'=\' | head -2 > tmp.txt')

    os_name = ""
    with open("tmp.txt", "r") as system_details:
        for line in system_details:
            os_name += line + " "
    
    os.system(f'echo "Operating System:{tabs}{os_name}')

# Identify total drive storage, storage used/free
def storage_info():
    print("TODO")

# Identify CPU model, number of processors/cores
def processor_info():
    print("TODO")

# Identify total and available RAM
def mem_info():
    print("TODO")
    
# Display all specified system information into a single report
def main():
    os.system('clear')
    os.system('echo "System Report - $(date \'+%B %d, %Y\')"')

    device_info()
    network_info()
    os_info()
    storage_info()
    processor_info()
    mem_info()

main()