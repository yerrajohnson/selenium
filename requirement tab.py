from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Import login details
from logindetails import LOGIN_URL, USERNAME, PASSWORD

# Initialize the Chrome WebDriver
def initialize_driver():
    driver = webdriver.Chrome()
    return driver

# Function to open the login page
def open_login_page(driver):
    print("Opening login page...")
    driver.get(LOGIN_URL)
    driver.maximize_window()


# Function to log in
def login(driver):
    wait = WebDriverWait(driver, 10)

    print("Filling in login details...")
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))

    email_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    print("Clicking Sign In...")
    signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    signin_button.click()

# Function to start the project
def start_project(driver):
    wait = WebDriverWait(driver, 10)

    print("Clicking Get Started...")
    get_started_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="text-left border rounded-md bg-white w-1/2"]//button[@type="button"]')))
    get_started_button.click()

# Function to validate the pop-up fields
def validate_popup_fields(driver):
    wait = WebDriverWait(driver, 10)

    # Define the XPaths for the fields we want to validate
    field_validations = {
        "Your Name": '//input[@name ="userName"]',
        "Company Name": '//input[@name="companyName"]',
        "Software Market": '//button[@name="softwareMarket"]',
        "Project Name": '//input[@name="projectName"]',
        "Project Description": '//textarea[@name="projectDesc"]'
    }

    print("Validating pop-up fields...")

    # Iterate through each field and check if it's present in the pop-up
    for field_name, xpath in field_validations.items():
        try:
            field_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if field_element.is_displayed():
                print(f"{field_name} is present.")
            else:
                print(f"{field_name} is not visible.")
        except TimeoutException:
            print(f"{field_name} is NOT present in the pop-up.")
        except Exception as e:
            print(f"Error checking {field_name}: {str(e)}")

    print("Filling in company name...")
    company_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="companyName"]')))
    company_name = "Backflipt"
    company_name_field.send_keys(company_name)

    print("Clicking dropdown options...")
    dropdown_options = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Digital Adoption Platforms")]')))
    dropdown_options.click()

    print("Filling in project name...")
    project_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="projectName"]')))
    project_name = "Barcelona-Project-UI"
    project_name_field.send_keys(project_name)

    print("Filling in project description...")
    project_desc_field = wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@name="projectDesc"]')))
    project_desc = "Barcelona-Project-UI"
    project_desc_field.send_keys(project_desc)

    print("Clicking Get Started in the popup...")
    get_started_button_popup = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Get Started")]')))
    get_started_button_popup.click()

    time.sleep(10)  # Wait for any transitions to complete

# Function to generate requirements
def generate_requirements(driver):
    wait = WebDriverWait(driver, 10)

    print("Clicking Generate Requirements...")
    generate_requirements_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Generate Requirements")]')))
    generate_requirements_button.click()

# Function to process tabs and extract elements
def process_tabs(driver):
    wait = WebDriverWait(driver, 10)
    tabs_xpath = "//div[@class='flex space-x-4 border-b border-gray-200']//button[@type='button']"
    main_elements_xpath = "//div[@class='mt-0.5 text-gray-700']"
    sub_element_xpath = "//p[@class='font-bold mb-2 text-gray-700']"

    # Switch between tabs and retrieve elements
    print("Switching between tabs...")
    tabs = wait.until(EC.presence_of_all_elements_located((By.XPATH, tabs_xpath)))

    for index, tab in enumerate(tabs):
        tab_class = tab.get_attribute('class')

        # Skip disabled tabs
        if 'disabled-form' in tab_class:
            print(f"Tab {index + 1} is disabled. Skipping...")
            continue

        # Click the tab if it's not the first one
        if index != 0:
            tab.click()
            print(f"Switched to Tab {index + 1}...")

        # Wait for main elements in the current tab
        main_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, main_elements_xpath)))

        # Process the first main element
        if main_elements:
            first_main_element = main_elements[0]
            print(f"First main element: {first_main_element.text}")

            # Try to retrieve and print sub-elements
            try:
                sub_elements = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, sub_element_xpath))
                )
                output_object = {
                    "element": first_main_element.text,
                    "subElements": [sub_element.text for sub_element in sub_elements]
                }
                print(json.dumps(output_object, indent=4))

                # Click the first main element to show its sub-elements
                first_main_element.click()

            except Exception as e:
                print(f"Error retrieving sub-elements for: {first_main_element.text}, {str(e)}")

            # Loop through remaining main elements
            for main_element in main_elements[1:]:
                try:
                    main_element.click()
                    print(f"Clicked main element: {main_element.text}")

                    # Wait for sub-elements to become visible
                    sub_elements = wait.until(
                        EC.visibility_of_all_elements_located((By.XPATH, sub_element_xpath))
                    )
                    output_object = OutputObject(
                        element=main_element.text,
                        sub_elements=[sub_element.text for sub_element in sub_elements]
                    )

                    # Use the to_dict() method to convert it to a dictionary before passing it to json.dumps
                    print(json.dumps(output_object.to_dict(), indent=4))

                    time.sleep(5)  # Collapse main element again
                    main_element.click()

                except StaleElementReferenceException:
                    print(f"Stale element: {main_element.text}, retrying...")
                    main_elements = wait.until(
                        EC.presence_of_all_elements_located((By.XPATH, main_elements_xpath))
                    )
                    main_element = main_elements[1]  # Update reference to the main element

# Function to collect data from the shortlist vendors
def collect_shortlist_vendors(driver):
    wait = WebDriverWait(driver, 10)
    print("Collecting shortlist vendors...")

    try:
        # Wait for vendor elements to become visible
        vendor_counts = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//h5[@class='card-title text-lg font-semibold ml-3']"))
        )
        vendor_values = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//h5[@class='card-count text-lg w-7 font-semibold']"))
        )

        # Ensure there are an equal number of vendors and values
        if len(vendor_counts) != len(vendor_values):
            print("Mismatch between the number of vendor names and vendor values!")
        else:
            keys = [vendor.text for vendor in vendor_counts]  # Vendor names are treated as strings
            values = [value.text for value in vendor_values]  # Vendor values (counts) are strings

            result_dict = {}
            for i in range(len(keys)):
                result_dict[keys[i]] = values[i]  # Keep vendor names and counts as strings

            json_result = json.dumps(result_dict, indent=4)
            print("Shortlist Vendors JSON Result:")
            print(json_result)

    except Exception as e:
        print(f"Error while collecting vendors: {str(e)}")

# Function to sign out
def sign_out(driver):
    wait = WebDriverWait(driver, 10)

    print("Signing out...")
    profile_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='dropdownTopButton']")))
    profile_icon.click()

    time.sleep(5)

    signout_option = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='group flex items-center px-4 py-2 cursor-pointer rounded-t-lg bg-white hover:!bg-[#0AB6FF] !text-gray-700 hover:!text-white']")))
    signout_option.click()

    time.sleep(5)

    signout_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Sign Out']")))
    signout_button.click()

    print("Successfully signed out.")

def main():
    driver = initialize_driver()

    try:
        open_login_page(driver)
        login(driver)
        start_project(driver)
        validate_popup_fields(driver)
        generate_requirements(driver)
        process_tabs(driver)
        collect_shortlist_vendors(driver)
        sign_out(driver)

    finally:
        driver.quit()

class OutputObject:
    def __init__(self, element, sub_elements):
        self.element = element
        self.sub_elements = sub_elements

    # Method to convert object to dictionary
    def to_dict(self):
        return {
            "element": self.element,
            "subElements": self.sub_elements
        }

    def __repr__(self):
        return f"OutputObject(element={self.element}, sub_elements={self.sub_elements})"



if __name__ == "__main__":
    main()