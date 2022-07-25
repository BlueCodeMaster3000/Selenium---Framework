from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# running test in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# option to ignore certificate error / safety error
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/kacperbiegajlo/Desktop/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(2)

# executing Java Script to scroll down the website
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0,-700);")

# making screenshot
driver.get_screenshot_as_file("screen.png")


