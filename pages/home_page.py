from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators

class HomePage(BasePage):
    """
        Strona domowa
    """

    def click_register_btn(self):
        el = self.driver.find_element(*HomePageLocators.register_button_hp)
        el.click()


    def _verify_page(self):
        # Weryfikuję, czy strona ma poprawny tytuł
        # Czekam na przycisk "Zarejestruj"
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(HomePageLocators.register_button_hp))
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(HomePageLocators.register_button_hp))
        assert "Praca - Pracuj.pl" in self.driver.title
        print("Weryfikacja strony HomePage")