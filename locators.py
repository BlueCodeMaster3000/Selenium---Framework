from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pathlib import Path

service_obj = Service(Path("./chromedriver/chromedriver").resolve())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText - locators supported by Selenium
driver.find_element(By.NAME, "email").send_keys("Pog@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Poggolini")
driver.find_element(By.ID, 'exampleCheck1').click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSSSelector -  tagname[attribute='value'] -> input[type='submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Kacper')
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1) # female selected
dropdown.select_by_visible_text("Female") # female selected
# dropdown.select_by_value() if there is value attribute you can also select it with that method


driver.find_element(By.XPATH, "//input[@type='submit']").click()
outcome = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(outcome)
assert "Success" in outcome
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
# driver.close()