from selenium import webdriver

driver=webdriver.Chrome()

print(driver.timeouts.page_load)
print(driver.timeouts.script)
print(driver.timeouts.implicit_wait)