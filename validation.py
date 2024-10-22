from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
username="user1@market2.idc.com"
password="Welcome17!"
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
driver.find_element(By.ID, "username").send_keys(username)
email=driver.find_element(By.XPATH,"//label[@class='form-text-box-label']")
print(email.text,"Field is present in the page")
driver.find_element(By.ID, "password").send_keys(password)
password=driver.find_element(By.XPATH,"//label[@for='password']")
print(password.text,"Field is present in the page")
button=driver.find_element(By.XPATH,"//button[@class='button primary']")
print(button.text,"Button is present in the page")
forgot=driver.find_element(By.XPATH, "(//a[contains(text(), 'I forgot my password.')])[2]")
print(forgot.text,"Link is present in the page")
driver.find_element(By.CLASS_NAME, "button.primary").click()
time.sleep(5)
if email and password and button and forgot:
    print("this page contains EMAIL,PASSWORD,LOGIN BUTTON and FORGOT PASSWORD")
    print("this is a login page")
else:
    print("Not a login page")
# print(button.text)
# email1=driver.find_element(By.CLASS_NAME, "form-text-box-label")
# print(email1.text)
# password1=driver.find_element(By.XPATH, "//label[@for='password']")
# print(password1.text)