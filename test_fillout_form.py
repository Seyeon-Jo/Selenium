from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Open a test form website
print("Opening form website")
driver.get('https://www.seleniumeasy.com/test/input-form-demo.html')

# Wait for the form to load
wait = WebDriverWait(driver, 10)

# Fill out the form
print("Filling out the form")
wait.until(EC.presence_of_element_located((By.NAME, 'first_name'))).send_keys('John')
wait.until(EC.presence_of_element_located((By.NAME, 'last_name'))).send_keys('Doe')
wait.until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys('john.doe@example.com')
wait.until(EC.presence_of_element_located((By.NAME, 'phone'))).send_keys('1234567890')
wait.until(EC.presence_of_element_located((By.NAME, 'address'))).send_keys('123 Main St')
wait.until(EC.presence_of_element_located((By.NAME, 'city'))).send_keys('Anytown')

# Note: Adjust the state selection method if needed
state_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'state')))
for option in state_dropdown.find_elements_by_tag_name('option'):
    if option.text == 'California':
        option.click()
        break

wait.until(EC.presence_of_element_located((By.NAME, 'zip'))).send_keys('90210')
wait.until(EC.presence_of_element_located((By.NAME, 'website'))).send_keys('www.example.com')
wait.until(EC.presence_of_element_located((By.NAME, 'hosting'))).send_keys('no')
wait.until(EC.presence_of_element_located((By.NAME, 'comment'))).send_keys('This is a test comment.')

# Submit the form
print("Submitting the form")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

# Wait for a few seconds
time.sleep(3)

# Close the browser
print("Quitting browser")
driver.quit()

print("Script completed successfully")
