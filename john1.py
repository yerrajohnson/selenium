from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import copy


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

def generate_requirements(driver):
    wait = WebDriverWait(driver, 10)

    # Function to generate requirements

    print("Clicking Generate Requirements...")
    generate_requirements_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Generate Requirements")]'))
    )
    print(generate_requirements_button.text)
    generate_requirements_button.click()
    time.sleep(10)
    # Wait for the requirement button to be clickable
    requirement_button = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//a[@class='flex group relative mt-1 p-1.5 text-sm rounded transition-all duration-300 text-gray-500']"))
    )
    requirement_button.click()

    # Wait for the elements to be present
    elements = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//span[@class='truncate']"))
    )
    element_list=[]
    subelements_list=[]
    for element in elements:
        element_list.append(element.text)
        # print(element.text)
        element.click()
        time.sleep(2)
        sub_elements=wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH,".//p[@class='font-semibold text-gray-700 my-1']"))
        )
        time.sleep(3)
        list=[]
        for i in sub_elements:
            text = i.text.strip()  # Strip leading/trailing whitespace
            if text:  # Check if the text is not empty
                list.append(text)

        subelements_list.append(list)
        element.click()

    dict={}
    t = 0
    for i in range(len(element_list)):
        for j in range(len(subelements_list[i])):
            sub = {}
            sub["element"] = element_list[i]
            sub["sub_element"]= subelements_list[i][j]
            dict[t] = sub.copy()
            t+=1
    result=json.dumps(dict,indent=4)
    print(result)


def main():
    driver = initialize_driver()

    try:
        open_login_page(driver)
        login(driver)
        start_project(driver)
        validate_popup_fields(driver)
        generate_requirements(driver)
        # process_tabs(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()