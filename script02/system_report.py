#!/bin/python3.9

###
#   Tri Tran
#   NSSA-221.03
#   Friday, February 21, 2024
###

import os
import platform

tabs = "\t\t\t\t\t" # Define standard tabbing across entire report

# Identify hostname and domain
def device_info():
    print("\nDevice Information")

    print("Hostname: " + tabs, end="")
    os.system("sleep 0.1 && hostname -s")

    print("Domain: " + tabs, end="")
    os.system("sleep 0.1 && domainname")


# Identify IP address, gateway, network mask, primary/secondary DNS
def network_info():
    print("TODO")

# Identify operating system/version and kernel version
def os_info():
    print("TODO")

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
    os.system("clear")
    print("System Report - ", end="")
    os.system("sleep 0.1 && date '+%B %d, %Y'")
    print("\n")

    device_info()
    network_info()
    os_info()
    storage_info()
    processor_info()
    mem_info()

main()