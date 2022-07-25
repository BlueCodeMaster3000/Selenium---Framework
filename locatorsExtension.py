from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")

# Linktext method / tag <a
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# also partial link text works with only "password?

# example for finding element via XPATH by Parent/child tags
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("PoggyWoggy")

# with CSS if you want to do parent/child traverse you use whitespace
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("PoggyWoggy")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# locator based on text alone
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
