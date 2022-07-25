import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
# 5 seconds of wait till element shows up on page
# if it is displayed faster then wait will be shorter
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count > 0 # to confirm that there are some search results
for product in products:
    # you can also get names here with actualList.append(product.find_element(By.XPATH, "div/h4").text)
    product.find_element(By.XPATH, "div/button").click()

# checking list of searched items
foundProducts = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
for foundProduct in foundProducts:
    actualList.append(foundProduct.text)

assert actualList == expectedList
#####

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
# example of explicit wait that will override implicit wait
# / used in case that you expect that one element wll take longer to show
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Sum validation
prices = driver.find_elements(By.XPATH, "//td[5]/p[@class='amount']")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

# totalAmount vs discountedAmount
discountedAmount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

assert totalAmount > discountedAmount
#driver.close()