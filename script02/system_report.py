#!/bin/python3.9

###
#   Tri Tran
#   NSSA-221.03
#   Friday, February 21, 2025
###

# Note: When using print() and os.system(), the command output was coming before print statements
# So everything is done using echo

import os
import sys

# Define standard tabbing across entire report
tabs_2 = "\t\t"
tabs_3 = "\t\t\t"
tabs_4 = "\t\t\t\t"

# Identify hostname and domain
def device_info():
    print("\nDevice Information")
    os.system(f'echo "Hostname:{tabs_3}$(hostname -s)"')
    os.system(f'echo "Domain:{tabs_3}\t$(domainname)"')


# Identify IP address, gateway, network mask, primary/secondary DNS
def network_info():
    print("\nNetwork Information")
    os.system(f'echo "IP Address:{tabs_3}$(hostname -I)"')
    os.system(f'echo "Gateway:{tabs_3}$(ip route show 0.0.0.0/0 | awk \'{{print $3}}\')"')
    os.system(f'echo "Network Mask:{tabs_3}$(route | awk \'$2 == \"0.0.0.0\" {{print $3}}\')"')
    os.system(f'echo "DNS1:{tabs_4}$(cat /etc/resolv.conf | awk \'$1 == \"nameserver\" {{print $2; exit}}\')"')
    os.system(f'echo "DNS1:{tabs_4}$(cat /etc/resolv.conf | awk \'$1 == \"nameserver\" {{count++; if (count == 2) print $2}}\')"')

# Identify operating system/version and kernel version
def os_info():
    print("\nOperating System Information")
    os.system('cat /etc/os-release | cut -d\'=\' -f2 | tr -d \'"\' | head -5 > tmp.txt')

    os_name = ""
    os_version = ""
    i = 0
    # The first five lines of os-release are NAME, VERSION, ID, ID_LIKE, VERSION_ID
    with open("tmp.txt", "r") as system_details:
        for line in system_details:
            if (i == 0 or i == 1):
                os_name += line.strip() + " "
            elif(i == 4):
                os_version = line.strip()
            
            i += 1
    
    os.system(f'echo "Operating System:{tabs_2}{os_name}"')
    os.system(f'echo "OS Version:{tabs_3}{os_version}"')
    os.system(f'echo "Kernel Version:{tabs_3}$(uname -r)"')
    os.system('rm tmp.txt')

# Identify total drive storage, storage used/free
def storage_info():
    print("\nStorage Information")
    os.system(f'echo "System Drive Total:{tabs_2}$(df -h --total | grep total | awk \'{{print $2}}\')"')
    os.system(f'echo "System Drive Used:{tabs_2}$(df -h --total | grep total | awk \'{{print $3}}\')"')
    os.system(f'echo "System Drive Free:{tabs_2}$(df -h --total | grep total | awk \'{{print $4}}\')"')

# Identify CPU model, number of processors/cores
def processor_info():
    print("\nProcessor Information")
    # cut takes everything after the colon and xargs strips whitespace
    os.system(f'echo "CPU Model:{tabs_3}$(lscpu | grep \"Model name\" | cut -d\':\' -f2 | xargs)"')
    os.system(f'echo "Number of processors:{tabs_2}$(nproc --all)"')
    os.system(f'echo "Number of cores:{tabs_2}$(lscpu | grep \"Core(s)\" | cut -d\':\' -f2 | xargs)"')

# Identify total and available RAM
def mem_info():
    print("\nMemory Information")
    # After xargs, everything is crammed into a single line so $1 is total ram, $2 is kB, $3 is available ram, $4 is kB
    os.system(f'echo "Total RAM:{tabs_3}$(cat /proc/meminfo | cut -d\':\' -f2 | xargs | awk \'{{print $1, $2; exit}}\')"')
    os.system(f'echo "Available RAM:{tabs_3}$(cat /proc/meminfo | cut -d\':\' -f2 | xargs | awk \'{{print $3, $4}}\')"')

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