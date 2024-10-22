from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import copy
from selenium.webdriver import ActionChains
import re
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

# def generate_requirements(driver):
#     wait = WebDriverWait(driver, 10)
#     action = ActionChains(driver)  # Create an instance of ActionChains
#     # Function to generate requirements
#
#     print("Clicking Generate Requirements...")
#     generate_requirements_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Generate Requirements")]'))
#     )
#     print(generate_requirements_button.text)
#     generate_requirements_button.click()
#     time.sleep(10)
#     # Wait for the requirement button to be clickable
#     requirement_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH,
#                                     "//a[@class='flex group relative mt-1 p-1.5 text-sm rounded transition-all duration-300 text-gray-500']"))
#     )
#     requirement_button.click()
#
#     # Wait for the elements to be present
#     elements = wait.until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "//span[@class='truncate']"))
#     )
#     element_length=len(elements)
#     # element_list=[]
#     # subelements_list=[]
#     for i in range(element_length):
#         # element_list.append(element.text)
#         # print(element.text)
#         elements[i].click()
#         time.sleep(5)
#         sub_elements=wait.until(
#             EC.presence_of_all_elements_located(
#                 (By.XPATH,"//p[@class='font-semibold text-gray-700 my-1']"))
#         )
#         for sub_element in sub_elements:
#             # Perform the hover action
#             action.move_to_element(sub_element).perform()
#             time.sleep(5)
#             icon=wait.until(
#             EC.presence_of_all_elements_located(
#                 (By.XPATH,"//a[@class='group/edit absolute right-2 invisible group-hover/item:visible cursor-pointer']"))
#         )
#             time.sleep(5)
#             for k in icon:
#                 if k.is_displayed():  # Ensure the icon is visible before clicking
#                     k.click()
#                     time.sleep(5)  # Optional delay after clicking
#
def generate_requirements(driver):
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)

    print("Clicking Generate Requirements...")
    generate_requirements_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Generate Requirements")]'))
    )
    generate_requirements_button.click()
    time.sleep(10)  # Adjust as needed

    requirement_button = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//a[@class='flex group relative mt-1 p-1.5 text-sm rounded transition-all duration-300 text-gray-500']"))
    )
    requirement_button.click()

    # Main loop for elements
    while True:
        try:
            elements = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[@class='truncate']"))
            )

            for element in elements:
                element.click()
                time.sleep(5)  # Adjust as needed

                # Re-fetch sub-elements after clicking
                sub_elements = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, "//p[@class='font-semibold text-gray-700 my-1']"))
                )

                for sub_element in sub_elements:
                    action.move_to_element(sub_element).perform()
                    time.sleep(5)  # Adjust as needed

                    # Re-fetch icons
                    icons = wait.until(
                        EC.presence_of_all_elements_located(
                            (By.XPATH, "//a[@class='group/edit absolute right-2 invisible group-hover/item:visible cursor-pointer']"))
                    )

                    for icon in icons:
                        if icon.is_displayed():  # Ensure the icon is visible before clicking
                            icon.click()
                            time.sleep(5)  # Optional delay after clicking

            break  # Exit the loop if successful
        except StaleElementReferenceException:
            print("StaleElementReferenceException caught. Retrying...")
            time.sleep(2)  # Wait before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit on any other error

            # k=j.text.strip()
            # if k:
            #     subelements_list.append(k)
            #     print(subelements_list)
    #     time.sleep(3)
    #     list=[]
    #     for i in sub_elements:
    #         text = i.text.strip()  # Strip leading/trailing whitespace
    #         if text:  # Check if the text is not empty
    #             list.append(text)
    #
    #     subelements_list.append(list)
    #     element.click()
    #
    # dict={}
    # t = 0
    # for i in range(len(element_list)):
    #     for j in range(len(subelements_list[i])):
    #         sub = {}
    #         sub["element"] = element_list[i]
    #         sub["sub_element"]= subelements_list[i][j]
    #         dict[t] = sub.copy()
    #         t+=1
    # result=json.dumps(dict,indent=4)
    # print(result)
def total_requirements(driver):
    # XPaths for tabs and elements
    tabs_xpath = "//div[@class='flex space-x-4 border-b border-gray-200']//button[@type='button']"
    main_elements_xpath = "//div[@class='mt-0.5 text-gray-700']"
    sub_element_xpath = "//p[@class='font-bold mb-2 text-gray-700']"

    # Switch between tabs
    tabs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, tabs_xpath))
    )

    # Dictionary to hold the output as a JSON object-like variable
    output_data = {}

    # Index counter for output dictionary keys
    output_index = 0

    # Loop through all tabs
    for index, tab in enumerate(tabs):
        tab_class = tab.get_attribute('class')

        # Get the axis (tab name or label) for the current tab
        tab_name = tab.text.strip()  # You can customize this depending on how you identify the tab

        # Skip the tab if it's disabled
        if 'disabled-form' in tab_class:
            print(f"Tab {index + 1} is disabled. Skipping...")
            continue

        # Click the tab to activate it (if it's not the default first tab)
        if index != 0:
            tab.click()
            print(f"Switched to Tab {index + 1}: {tab_name}...")

        # Wait for the main elements in the current tab
        main_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, main_elements_xpath))
        )

        # Loop through the main elements and sub-elements
        for i, main_element in enumerate(main_elements):
            try:
                # Click the main element to expand its sub-elements
                if i != 0:  # The first element is already expanded
                    main_element.click()
                    print(f"Clicked main element: {main_element.text}")

                # Wait for the sub-elements to become visible after clicking
                sub_elements = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.XPATH, sub_element_xpath))
                )

                # If there is more than 1 sub-element, output each separately
                for sub_element in sub_elements:
                    # Clean the element text to remove any trailing integer values
                    cleaned_element_text = re.sub(r' \d+$', '', main_element.text)

                    # Store the cleaned element text in the output data
                    output_data[output_index] = {
                        "axis": tab_name.lower(),  # Assign the current tab name as the axis
                        "element": cleaned_element_text,  # Use cleaned element text for the "element" key
                        "subElements": sub_element.text  # Use original sub-element text
                    }
                    output_index += 1  # Increment the output index

                # Optionally, add a delay for visual purposes (e.g., time.sleep(5))
                main_element.click()  # Collapse the element after processing

            except StaleElementReferenceException:
                print(f"Stale element: {main_element.text}, retrying...")
                # Re-locate the main element and retry the operation
                main_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, main_elements_xpath))
                )
                main_element = main_elements[i]
            except Exception as e:
                print(f"Error retrieving sub-elements for: {main_element.text}, {str(e)}")

    # The output data is now stored in a variable `output_data`
    # You can use this JSON-like variable further as needed
    json_output = json.dumps(output_data, indent=4)

    # Optional: You can print or return the JSON-like output variable for further processing
    print(json_output)
    time.sleep(5)

def main():
    driver = initialize_driver()

    try:
        open_login_page(driver)
        login(driver)
        start_project(driver)
        validate_popup_fields(driver)
        generate_requirements(driver)
        total_requirements(driver)
        # process_tabs(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()