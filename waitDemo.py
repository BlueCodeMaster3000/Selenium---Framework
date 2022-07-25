import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path

service_obj = Service(Path("./chromedriver/chromedriver").resolve())
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
# 5 seconds of wait till element shows up on page
# if it is displayed faster then wait will be shorter
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count > 0 # to confirm that there are some search results
for product in products:
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
