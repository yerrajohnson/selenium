from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up options for headless browsing (optional)
options = Options()
options.headless = True  # Comment this line if you want to see the browser window

# Initialize the WebDriver
#service = Service("C:\\path\\to\\chromedriver.exe")  # Adjust the path to your chromedriver
driver = webdriver.Chrome()

try:
    # URL of the login page
    login_url = "https://qa.idc.com/buyer-platform/login"

    # Navigate to the login page
    driver.get(login_url)

    # Wait for the title to confirm navigation
    WebDriverWait(driver, 10).until(EC.title_contains("Login"))

    # Validate by checking the title
    if "Login" in driver.title:
        print("Successfully navigated to the Login page.")
    else:
        print("Failed to navigate to the Login page: Title does not match.")

    # Wait for the login form to be present
    try:
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'loginForm'))  # Adjust ID as needed
        )
        print("Successfully found the login form.")
    except Exception as e:
        print("Login form not found:", e)

finally:
    # Clean up
    driver.quit()
