from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
url="https://qa.idc.com/buyer-platform/login"
driver=webdriver.Chrome()
driver.get(url)
a=driver.find_element(By.CLASS_NAME,"form-text-box-label")
print(a.text)


