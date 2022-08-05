import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path

service_obj = Service(Path("./chromedriver/chromedriver").resolve())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() # method to check if item is selected
        break

radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio1":
        radioButton.click()
        assert radioButton.is_selected()
        break

time.sleep(2) # used sleep to wait for assertion from previous segment

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[1].click() # also works if index does not change
assert radioButtons[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()