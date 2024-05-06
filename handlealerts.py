import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.set_page_load_timeout(60)

driver.set_script_timeout(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()

time.sleep(2)

driver.find_element(By.XPATH,"").size

alert=driver.switch_to.alert

print(alert.text)

assert "JS Alert" in alert.text

time.sleep(2)
# to accept alert
alert.accept()

# to cancel alert or dismiss or no button
#alert.dismiss()

# to type in alert prompt box
#alert.send_keys("name")



