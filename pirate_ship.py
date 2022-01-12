# Test to view whether we can directly send requests to PirateShip's private API
# Doesn't work currently.

import requests
import os
import urllib.request

PIRATE_URL = "https://ship.pirateship.com/"
EXPORT_URL = "https://ship.pirateship.com/batch_complete/export"

# Create a folder in the user's current working directory
# Named "customer_tracking" for now
def create_directory():
    cwd = os.getcwd()
    final = os.path.join(cwd, 'customer_tracking')
    if not os.path.exists(final):
        os.makedirs(final)
    return final

if __name__ == "__main__":

    # Get user credentials
    username = input("Enter your email: ")
    password = input("Enter your password: ")

    # Create requests Session
    s = requests.Session()

    # Set session data
    data = {"username": username, "password": password}

    # Send user credentials to successfully login
    r = s.post(PIRATE_URL, data=data)

    # Testing shit to download this user's tracking data
    url = EXPORT_URL + '?shipment_id=XXXXXXXXXX'
    file = s.get(url, allow_redirects=True)
    print(file.headers)

    # Create directory if it doesn't exist and get the path to that folder
    path = create_directory()
    print(file.content)

    file_name = ""

    # Download the file
    with urllib.request.urlopen(url) as response, open(file_name, "wb") as output_file:
        data = response.read()
        output_file.write(data)


