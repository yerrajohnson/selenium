from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json
username="user1@market2.idc.com"
password="Welcome17!"
# Set up options for headless browsing (optional)
options = Options()
options.headless = True  # Comment this line if you want to see the browser window

# Initialize the WebDriver
#service = Service("C:\\path\\to\\chromedriver.exe")  # Adjust the path to your chromedriver
driver = webdriver.Chrome()

try:
    # URL of the login page
    login_url = "https://qa.idc.com/buyer-platform/home"

    # Navigate to the login page
    driver.get(login_url)

    # Wait for a few seconds to ensure the page loads completely
    time.sleep(3)

    # Validate by checking the title or a specific element
    if "Login" in driver.title:
        print("Successfully navigated to the Login page.")
    else:
        print("Failed to navigate to the Login page: Title does not match.")

    # Optionally, check for a specific element on the login page
    try:
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CLASS_NAME, "button.primary").click()
        print("Successfully found the login form.")
        time.sleep(10)
        company_name=driver.find_elements(By.XPATH, "//h5[@class='card-title text-lg font-semibold ml-3']")
        company_rank=driver.find_elements(By.XPATH,"//h5[@class='card-count text-lg w-7 font-semibold']")
        keys=[]
        values=[]
        for i in range(len(company_rank)):
            keys.append(company_rank[i].text)
            values.append(company_name[i].text)
        result_dict={}
        count_companies = driver.find_element(By.XPATH, "//span[@class='text-3xl font-semibold']")
        print(count_companies.text)
        if int(count_companies.text) == len(keys):
            for i in range(len(keys)):
                result_dict[int(keys[i])]=values[i]
            json_result=json.dumps(result_dict,indent=4)
            print(json_result)
        json_dict=json.loads(json_result)
        print(json_dict)
        # final_result=[]
        # for i,j in json_dict.items():
        #     item={i : j}
        #     final_result.append(item)
        # print(final_result)
        final_result = {}
        index = 0  # Initialize the index

        # Create the desired output format
        for item in json_dict:
            for rank, company_name in item.items():
                final_result[index] = {
                    "rank": int(rank),
                    "company_name": company_name.lower()  # Convert to lowercase
                }
                index += 1  # Increment the index

        # Convert the final result to JSON format
        final_result_json = json.dumps(final_result, indent=3)

        # Print the JSON string
        print(final_result_json)
        #


        
    except Exception as e:
        print("Login form not found:", e)


finally:
    # Clean up
    driver.quit()
