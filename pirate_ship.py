import requests
import os

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
    url = EXPORT_URL + '?shipment_id=177161551'
    file = s.get(url, allow_redirects=True)
    print(file.headers)

    # Create directory if it doesn't exist and get the path to that folder
    path = create_directory()
    #print(file.content)

    # Download the file
    #open(os.path.join(path, 'file.xlsx'), 'wb').write(file.content)



