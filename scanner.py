#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

# prompt user
print("\n-------------------------------------------------")
print("\n   ____  _ _ _                                   \n  / __ \| (_| )                                  \n | |  | | |_|/ ___   _ __  _ __ ___   __ _ _ __  \n | |  | | | | / __| | '_ \| '_ ` _ \ / _` | '_ \ \n | |__| | | | \__ \ | | | | | | | | | (_| | |_) |\n  \____/|_|_| |___/ |_| |_|_| |_| |_|\__,_| .__/ \n                                          | |    \n                                          |_|    ")

print("\n-------------------------------------------------")
print("\nWelcome to Oli's nmap scanner.")

# user inputs target IP address
target_ip = input("\nIP Address (target IP): ")

print("\nPerforming scan on target: " + target_ip)
type(target_ip)

resp = input("""\nPlease choose what type of scan to perform:
             1) SYN/ACK Scan
             2) UDP Scan
             3) AGGRESSIVE Scan""")

print("Now performing a " + resp + " scan on " + target_ip)