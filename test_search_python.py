from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup ChromeDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Google homepage
print("Opening Google")
driver.get('https://www.google.com')

# Search for 'Python programming'
print("Finding search box")
search_box = driver.find_element(By.NAME, 'q')
print("Typing 'Python programming'")
search_box.send_keys('Python programming')
print("Pressing Enter")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(3)

# Print titles of the first few search results
print("Printing titles of the first few search results")
titles = driver.find_elements(By.CSS_SELECTOR, 'h3')
for i, title in enumerate(titles[:5]):
    print(f"{i+1}. {title.text}")

# Close the browser
print("Quitting browser")
driver.quit()

print("Script completed successfully")
