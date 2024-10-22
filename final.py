from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up options for headless browsing (optional)
# options = Options()
# options.headless = True  # Comment this line if you want to see the browser window

# Initialize the WebDriver
#service = Service("C:\\path\\to\\chromedriver.exe")  # Adjust the path to your chromedriver
driver = webdriver.Chrome()
username="user1@market2.idc.com"
password="Welcome17!"
login_url = "https://qa.idc.com/buyer-platform/login"
driver.get(login_url)
time.sleep(3)
if "Login" in driver.title:
    print("Successfully navigated to the Login page.")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "button.primary").click()
    # time.sleep(10)

else:
    print("Login form not found:")








#     # Validate by checking the title or a specific element
#     if "Login" in driver.title:
#         print("Successfully navigated to the Login page.")
#     else:
#         print("Failed to navigate to the Login page: Title does not match.")
#
#     # Optionally, check for a specific element on the login page
#     try:
#         a=login_form = driver.find_element(By.ID, 'username')  # Adjust ID as needed
#         print("Successfully found the login form.")
#         print(a.text)
#     except Exception as e:
#         print("Login form not found:", e)
#
# finally:
#     # Clean up
#     driver.quit()
