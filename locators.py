from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Selektory strony głównej"""
    login_button = (By.XPATH, "//a[@title='Zaloguj się']")
    register_button_hp = (By.XPATH, "//a[@title='Załóż konto']")

class RegisterPageLocators():
    """ Selektory strony Rejestracja"""
    email_input = (By.XPATH, "//input[@type='email']")
    password_input = (By.XPATH, "//input[@type='password']")
    regulation_checkbox = (By.XPATH, "//label[contains(@class,'_34dTT')]")
    register_button = (By.XPATH, "//button[@data-test='button-registration'][contains(.,'Zarejestruj się')]")
    error_msg = (By.XPATH, "//div[@data-test='validation-summary-errors']")