from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Chrome options
chrome_options = webdriver.ChromeOptions()
# Comment out or remove the following line to show the UI
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup ChromeDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Google homepage
print("Opening Google")
driver.get('https://www.google.com')

# Search for 'Selenium'
print("Finding search box")
search_box = driver.find_element(By.NAME, 'q')
print("Typing 'Selenium'")
search_box.send_keys('Selenium')
print("Pressing Enter")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds then close the browser
time.sleep(5)

print("Quitting browser")
driver.quit()

print("Script completed successfully")
