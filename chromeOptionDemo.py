from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)