from pages.base_page import BasePage
from locators import RegisterPageLocators



class RegisterPage(BasePage):
    def fill_email(self, email):
        self.driver.find_element(*RegisterPageLocators.email_input).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*RegisterPageLocators.password_input).send_keys(password)

    def regulation_check_box(self):
        self.driver.find_element(*RegisterPageLocators.regulation_checkbox).click()

    def register_button_click(self):
        self.driver.find_element(*RegisterPageLocators.register_button).click()

    def find_errors(self, number_of_errors, errors_texts):
        errors_msgs = self.driver.find_elements(*RegisterPageLocators.error_msg)
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in errors_msgs:
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczna jest właściwa liczba błędów
        print("Liczba widocznych błędów na stronie: " + str(len(visible_error_notices)))
        assert len(visible_error_notices) == number_of_errors
        # Sprawdzam treść widocznych błędów
        errors_text_fact = []
        for i in range(len(visible_error_notices)):
            errors_text_fact.append(visible_error_notices[i].get_attribute("innerText"))
        print(errors_text_fact)
        assert errors_text_fact == errors_texts
