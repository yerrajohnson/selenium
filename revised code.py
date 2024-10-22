from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


def initialize_driver(headless=True):
    """Initialize the WebDriver."""
    options = Options()
    options.headless = headless  # Set to True for headless mode
    driver = webdriver.Chrome(options=options)
    return driver


def navigate_to_login(driver, url):
    """Navigate to the login page."""
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    return "Login" in driver.title


def login(driver, username, password):
    """Log into the application."""
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "button.primary").click()
    time.sleep(5)  # Wait for login to complete


def retrieve_company_data(driver):
    """Retrieve company names and ranks from the page."""
    try:
        # Wait for the companies count element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='text-3xl font-semibold']"))
        )

        company_name_elements = driver.find_elements(By.XPATH, "//h5[@class='card-title text-lg font-semibold ml-3']")
        company_rank_elements = driver.find_elements(By.XPATH, "//h5[@class='card-count text-lg w-7 font-semibold']")

        keys = [element.text for element in company_rank_elements]
        values = [element.text for element in company_name_elements]

        result_dict = {}
        count_companies = driver.find_element(By.XPATH, "//span[@class='text-3xl font-semibold']")

        if int(count_companies.text) == len(keys):
            for i in range(len(keys)):
                result_dict[int(keys[i])] = values[i]

        return result_dict
    except Exception as e:
        print("Error retrieving company data:", e)
        return {}


def format_result_as_json(result_dict):
    """Convert the result dictionary to a formatted JSON string."""
    final_result = {}
    index = 0
    for rank in result_dict:
        final_result[index] = {
            "rank": rank,
            "company_name": result_dict[rank].lower()  # Convert to lowercase
        }
        index += 1

    return json.dumps(final_result, indent=3)


def main():
    username = "user1@market2.idc.com"
    password = "Welcome17!"
    login_url = "https://qa.idc.com/buyer-platform/home"

    driver = initialize_driver()
    try:
        if navigate_to_login(driver, login_url):
            print("Successfully navigated to the Login page.")
            login(driver, username, password)
            print("Successfully found the login form.")

            result_dict = retrieve_company_data(driver)
            if result_dict:
                json_result = format_result_as_json(result_dict)
                print(json_result)
            else:
                print("No company data found.")
        else:
            print("Failed to navigate to the Login page: Title does not match.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
