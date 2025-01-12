from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import string
import time

# Function to generate random name
def generate_random_name(length=6):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Generate random first and last names
first_name = generate_random_name()
last_name = generate_random_name()

print(f"Generated Name: {first_name} {last_name}")

# Set up Chrome options (incognito mode)
options = Options()
options.add_argument("--incognito")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Navigate directly to the Google sign-up page
driver.get("https://accounts.google.com/signup")

# Wait for the page to load
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='firstName']"))
)

# Wait for the first name field to appear and enter the generated name
first_name_field = driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
time.sleep(random.uniform(1, 2))  # Simulate a human-like delay
first_name_field.send_keys(first_name)
print(f"Entered first name: {first_name}")

# Wait for a short break to simulate human interaction
time.sleep(random.uniform(1, 2))

# Wait for the last name field to appear and enter the generated last name
last_name_field = driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
time.sleep(random.uniform(1, 2))  # Simulate a human-like delay
last_name_field.send_keys(last_name)
print(f"Entered last name: {last_name}")

# Locate and click the "Next" button before the birthday page
next_button_before_birthday = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ"))
)
next_button_before_birthday.click()
print("Clicked the 'Next' button before the birthday page.")

# Select a random month from the dropdown
month_dropdown = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "month"))
)

# Create a Select object for the dropdown
select_month = Select(month_dropdown)

# Pick a random month (values 1 to 12 represent the months)
random_month = random.randint(1, 12)
select_month.select_by_value(str(random_month))
print(f"Selected month: {random_month}")

random_month = random.randint(1, 12)
select_month.select_by_value(str(random_month))
print(f"Selected month: {random_month}")

# Generate a random day between 1 and 25
random_day = random.randint(1, 25)

# Locate the day input field and enter the random day
day_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "day"))
)
day_input.send_keys(str(random_day))
print(f"Entered day: {random_day}")

year_field = driver.find_element(By.ID, "year")
year_field.send_keys("2000")

gender_dropdown = driver.find_element(By.ID, "gender")
select = Select(gender_dropdown)
select.select_by_value("1")
# Find the "Next" button and click it
next_button = driver.find_element(By.XPATH, "//button[@jsname='LgbsSe']")
next_button.click()

import time

# After filling out the dates and before closing the browser, add a delay
time.sleep(2)  # Wait for 5 seconds before closing

# Find the top checkbox and click it
# Find all checkboxes and click the first one
# Locate the first option containing '@' (likely to be an email)
first_email_option = driver.find_element(By.XPATH, "//div[contains(text(), '@')]")
first_email_option.click()

# Find the "Next" button and click it
next_button = driver.find_element(By.XPATH, "//button[@jsname='LgbsSe']")
next_button.click()


# Wait for a few seconds before closing the browser to simulate human behavior
time.sleep(5)


import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

password = generate_password()
print(f"Generated password: {password}")

# Locate the first password input field
password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
)

# Generate a random password
password = generate_password()

# Fill the password field with the generated password
password_field.send_keys(password)

print("First password entered.")

# Locate the second password input field (Confirm Password)
confirm_password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "PasswdAgain"))
)

# Fill the confirm password field with the same password
confirm_password_field.send_keys(password)

print("Confirm password entered.")

next_button = driver.find_element(By.XPATH, "//button[@jsname='LgbsSe']")
next_button.click()

time.sleep(3)

# Locate the phone number input field using the ID
phone_number_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "phoneNumberId"))
)

# Enter the phone number into the input field
phone_number_field.send_keys("7492872797")

print("Phone number entered.")




# Optionally, you can close the browser here
driver.quit()
