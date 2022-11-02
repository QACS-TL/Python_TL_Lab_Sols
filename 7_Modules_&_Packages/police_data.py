#! /bin/python
# Name:        police_data.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Get online Police Data.
"""
    Get and display Online Police Crime Data
"""

import sys
import requests

def getPoliceForces():
    """ Get List of English Police Forces by Region """
    base_url = r"https://data.police.uk/api/"
    full_url = base_url + "forces"
    force_data = requests.get(full_url)  # HTTP GET url page.

    for force in force_data.json():
        print(f"{force['id']:>30s}: {force['name']:<20s}")
    print()
    return None

def getCrimeByLoc():
    """ Display Police Crime data for a specific lat/long """
    date = input("Enter a date (eg. 2021-07): ") or "2021-07"
    lat = input("Enter a Latitude (eg. 51.506): ") or "51.506"
    lon = input("Enter a Longitude (eg. -0.075): ") or "-0.075"

    base_url = r"https://data.police.uk/api/"
    full_url = base_url + "crimes-at-location?lat=" + lat + "&lng=" + lon + "&date=" + date
    crime_data = requests.get(full_url)
    for crime in crime_data.json():
        print(f"{crime['category']}, {crime['location_type']}, "
              f"{crime['outcome_status']['category'] if crime['outcome_status'] else 'No Investigation'}, "
              f"{crime['location']['street']['name']}")
    print()
    return None

def main():
    """ The Main Program """
    menu = """     
        Police Data
        -----------
        1. List of Police Forces
        2. Crimes by location

    """
    while True:
        print(menu)
        option = input("Enter option (1-2, q=quit): ")

        if option == "1":
            getPoliceForces()
        elif option == "2":
            getCrimeByLoc()
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")


    return None

if __name__ == "__main__":
    main()
    sys.exit(0)