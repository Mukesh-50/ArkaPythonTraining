from selenium.webdriver.common.by import By

from BasePage import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD=(By.ID,"email1")
    PASSWORD_FIELD = (By.ID, "password1")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign in']")

    def login_to_application(self, user,password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(user)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()