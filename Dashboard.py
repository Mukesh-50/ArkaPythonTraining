from selenium.webdriver.common.by import By

from BasePage import BasePage


class Dashboard(BasePage):
    WELCOME_MSG=(By.XPATH,"//h4[@class='welcomeMessage']")

    def get_welcome_msg(self):
        return self.driver.find_element(*self.WELCOME_MSG).text
