import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
dropDownElements = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
print(len(dropDownElements))

for dropDownElement in dropDownElements:
    if dropDownElement.text == "India":
        dropDownElement.click()
        break



