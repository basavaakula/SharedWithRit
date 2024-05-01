# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # To run Chrome in headless mode (no GUI)
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model

# Path to the chromedriver executable
chromedriver_path = '/usr/lib/chromium-browser/chromedriver'

# Initialize the webdriver
driver = webdriver.Chrome(options=chrome_options)

# Corrected URL
driver.get("https://www.google.com")
print("Title of the page is:", driver.title)
#print("I am open")

driver.quit()