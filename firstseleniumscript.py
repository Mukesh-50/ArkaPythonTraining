import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()

driver.set_page_load_timeout(60)

driver.set_script_timeout(10)

driver.get("https://freelance-learn-automation.vercel.app/login")

driver.implicitly_wait(10)

print(driver.current_url)

print(driver.title)

username = driver.find_element(By.ID, "email1")

username.send_keys("admin@email.com")

driver.find_element(By.NAME, "password1").send_keys("admin@1234")

driver.find_element(By.CLASS_NAME, "submit-btn").click()

welcomemsg=driver.find_element(By.XPATH,"//h4[@class='welcomeMessage']").text

assert "Welcome" in welcomemsg

driver.find_element(By.XPATH,"//img[@alt='menu']").click()

driver.find_element(By.XPATH,"//button[text()='Sign out']").click()

status=WebDriverWait(driver,200).until(expected_conditions.url_contains("login"))

assert status
