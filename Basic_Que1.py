from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#cap = DesiredCapabilities.CHROME
#cap = ('binary_location'="C:\Users\YOGA\Documents\GitHub\Selenium_Revision\chrome-win64\chrome")
chrome_options = Options()
chrome_service = Service(r"C:\Users\YOGA\Documents\GitHub\Selenium_Revision\chromedriver")

#chrome_service.env.
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Bypass OS security model
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')

 
#chrome_options.binary_location("/home/codespace/.cache/selenium/chrome/linux64/124.0.6367.91/chrome")
driver = webdriver.Chrome(service= chrome_service)

driver.get("www.google.com")
print("I am open")