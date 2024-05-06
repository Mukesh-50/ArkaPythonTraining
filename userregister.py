import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.set_page_load_timeout(60)

driver.set_script_timeout(10)

driver.get("https://freelance-learn-automation.vercel.app/signup")

driver.implicitly_wait(10)

state = driver.find_element(By.XPATH, "//select[@name='state']")

button_status = driver.find_element(By.XPATH, "//button[text()='Sign up']").is_enabled()

assert button_status == False

dropdown = Select(state)

dropdown.select_by_index(3)

dropdown.select_by_value("Goa")

dropdown.select_by_visible_text("Karnataka")

hobbies = Select(driver.find_element(By.XPATH, "//select[@id='hobbies']"))

hobbies.select_by_visible_text("Playing");

hobbies.select_by_visible_text("Reading")

hobbies.select_by_visible_text("Swimming");
