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

parent=driver.current_window_handle

print(parent)

driver.find_element(By.XPATH,"//div[@class='social']//a[contains(@href,'linkedin')]").click()

allwindowhandles=driver.window_handles

print(allwindowhandles)

print(allwindowhandles[1])

driver.switch_to.window(allwindowhandles[1])

status=WebDriverWait(driver,20).until(expected_conditions.title_contains("Linked"))

assert status












