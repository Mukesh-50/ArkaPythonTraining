import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()

driver.set_page_load_timeout(60)

driver.set_script_timeout(10)

driver.get("https://freelance-learn-automation.vercel.app/login")

driver.implicitly_wait(10)

driver.switch_to.frame('frame_name')

driver.switch_to.frame(1)

driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])














