import requests
from bs4 import BeautifulSoup

# URL of the login page
login_url = "https://qa.idc.com/buyer-platform/login"

# Send a GET request to the login page
response = requests.get(login_url)
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Check for a specific element that indicates the login page (like a form or title)
    # This example checks for a title or a login form element
    if soup.title and "IDC.com - Buyer Platform" in soup.title.string:
        print("Successfully navigated to the Login page.")
    elif soup.find('form', {'id': 'loginForm'}):  # Adjust the form ID as needed
        print("Successfully navigated to the Login page.")
    else:
        print("Login page validation failed: Title or form not found.")
else:
    print(f"Failed to retrieve the login page. Status code: {response.status_code}")
