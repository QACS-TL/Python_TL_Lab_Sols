#! /bin/python
# Name:        display_unused_ports.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Display all the unused ports in the SERVICES file.
"""
    Display unused next ports from the SERVICES file.
"""


import sys

def main():
    if sys.platform == "win32":
        filename = r"C:\WINDOWS\System32\drivers\etc\services"
    else:
        filename = r"/etc/services"

    # Open file handle for reading in text mode.
    fh_in = open(filename, mode="rt")
    all_ports = set(range(1, 201))
    used_ports = set()

    # Iterate through file handle and read the services.
    for line in fh_in:
        if line.isspace(): continue
        if line.startswith("#"): continue

        fields = line.split("/") # Split line into list using '/'
        fields = fields[0].split() # Split 1st field using whitespace.
        port = int(fields[1]) # Index 1 is the port number.
        if port <= 200:
            used_ports.add(port)

    print(f"All ports = {all_ports}")
    print(f"Used ports = {used_ports}")
    print(f"Unused ports = {all_ports - used_ports}")

    fh_in.close()

if __name__ == "__main__":
    main()
    sys.exit(0)