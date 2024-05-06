import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Dashboard import Dashboard
from HomePage import HomePage
from LoginPage import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(60)
driver.set_script_timeout(10)
driver.get("https://freelance-learn-automation.vercel.app")
driver.implicitly_wait(10)

home_page=HomePage(driver);
home_page.click_login_link()

login_page=LoginPage(driver)
login_page.login_to_application("admin@email.com","admin@123")

#assert
dashboard=Dashboard(driver)
welcome_msg=dashboard.get_welcome_msg()

assert "Welcome" in welcome_msg

home_page.logout_from_application()

#assert logout is done