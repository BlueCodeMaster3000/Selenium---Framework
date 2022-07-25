from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.fullscreen_window()
# driver.maximize_window() also works
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.forward()
driver.close()
# so fast I dont even see what is going on SPEEEEEEEEED
