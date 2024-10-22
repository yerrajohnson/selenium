from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up options for headless browsing
options = Options()
options.headless = True

# Initialize the WebDriver
#service = Service("C:\Users\Administrator\Downloads\chromedriver-win64")  # Adjust the path to your chromedriver
driver = webdriver.Chrome()

# URL of the dynamic page
dynamic_url = "https://qa.idc.com/buyer-platform/login"

# Navigate to the page
driver.get(dynamic_url)

# Get the page source after JavaScript has rendered
html = driver.page_source

# Optionally parse with BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Get all HTML tags
all_tags = soup.find_all()
for tag in all_tags:
    print(tag)

# Clean up
driver.quit()
