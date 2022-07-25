from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[-1]) # used -1 to open last window since it should be the newest
print(driver.find_element(By.TAG_NAME, "h3").text) # this has to be performed in child window
driver.close()

driver.switch_to.window(windowsOpened[0])
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"
driver.close()