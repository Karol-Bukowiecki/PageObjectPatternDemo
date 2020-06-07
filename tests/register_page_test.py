from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
import unittest

class RegistrationTest(BaseTest):
    """
    Testy strony Rejestracja
    """
    def test_incorrect_email(self):
        print("Test rejestracji nowego użytkownika - błędny e-mail")
        # Tworzę instancję klasy HomePage, dzięki czemu zyskuję możliwość
        # korzystania z metod w niej zawartych
        hp = HomePage(self.driver)
        hp.click_register_btn()
        # Tworzę instancje klasy RegisterPage
        rp = RegisterPage(self.driver)
        # Wpisuje błędny email
        rp.fill_email("bledny.email.pl")
        # Wpisuje hasło
        rp.fill_password("password")
        # Potwierdzam checkbox od regulaminu
        rp.regulation_check_box()
        # Kliknij Zarejestruj
        rp.register_button_click()
        # Wyszukuję błędy na stronie
        rp.find_errors(1, ["Proszę wprowadzić adres e-mail"])



if __name__=="__main__":
    unittest.main(verbosity=3)
