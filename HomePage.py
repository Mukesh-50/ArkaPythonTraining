from selenium.webdriver.common.by import By

from BasePage import BasePage


class HomePage(BasePage):
    LOGIN_LINK = (By.XPATH, "//img[@alt='menu']")
    SIDE_MENU = (By.XPATH, "//button[normalize-space()='Log in']")
    LOGOUT_LINK=(By.XPATH,"//button[normalize-space()='Sign out']")

    def click_login_link(self):
        self.driver.find_element(*self.LOGIN_LINK).click()
        self.driver.find_element(*self.SIDE_MENU).click()

    def logout_from_application(self):
        self.driver.find_element(*self.LOGIN_LINK).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()