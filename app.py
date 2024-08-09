from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver_path = 'chromedriver.exe'  # Update with the path to your updated ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Function to login to Gmail
def login_to_gmail(email, password):
    driver.get('https://mail.google.com/')
    
    # Enter email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'identifier'))
    )
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    
    # Enter password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

# Function to mark all emails in Spam as "Not Spam"
def mark_emails_as_not_spam():
    # Navigate to Spam folder
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "#spam")]'))
    ).click()

    time.sleep(5)  # Wait for the Spam folder to load

    while True:
        try:
            # Find and open the first email in Spam
            email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.zA'))
            )
            email.click()

            # Mark email as "Not Spam"
            not_spam_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Not spam"]'))
            )
            not_spam_button.click()

            time.sleep(3)  # Wait for the action to complete
        except:
            # No more emails in Spam
            break

# Function to navigate to the Inbox
def go_to_inbox():
    inbox_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "#inbox")]'))
    )
    inbox_button.click()

# Main function
def main():
    email = 'your-email@gmail.com'  # Update with your email
    password = 'your-password'  # Update with your password

    try:
        login_to_gmail(email, password)
        mark_emails_as_not_spam()
        go_to_inbox()
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
