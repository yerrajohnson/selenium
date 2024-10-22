
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


def init_driver(headless=True):
    """Initialize the Chrome WebDriver."""
    options = Options()
    options.headless = headless
    driver = webdriver.Chrome(options=options)
    return driver


def login(driver, username, password, login_url):
    """Log in to the website."""

    driver.get(login_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "button.primary").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[@class='card-title text-lg font-semibold ml-3']")))


def extract_data(driver):
    """Extract data from the page and return it as a JSON string."""
    titles = driver.find_elements(By.XPATH, "//h5[@class='card-title text-lg font-semibold ml-3']")
    counts = driver.find_elements(By.XPATH, "//h5[@class='card-count text-lg w-7 font-semibold']")

    result_dict = {}
    for title, count in zip(titles, counts):
        result_dict[int(count.text)] = title.text

    return json.dumps(result_dict, indent=4)


def main():
    username = "user1@market2.idc.com"
    password = "Welcome17!"
    login_url = "https://qa.idc.com/buyer-platform/home"

    driver = init_driver()

    try:
        login(driver, username, password,login_url)
        json_result = extract_data(driver)
        print(json_result)

        # Optional: Get size or any additional information
        size = driver.find_element(By.XPATH, "//span[@class='text-3xl font-semibold']")
        print("Size:", size.text)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
