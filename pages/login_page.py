from pages.base_page import BasePage
from locators import HomePageLocators


class LoginPage(BasePage):
    def click_login_btn(self):
        el = self.driver.find_element(*HomePageLocators.login_button)
        el.click()
