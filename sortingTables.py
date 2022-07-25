from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browserSortedVeggies =[]

# clicking on column header to sort
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all vegetables names
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()
browserSortedVeggies.sort()

# assertion to check if list was sorted properly
assert originalBrowserSortedList == browserSortedVeggies

driver.close()
