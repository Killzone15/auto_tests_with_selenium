from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        substring = 'login'
        full_string = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма логина не найдена!'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            'Форма регистрации не найдена!'

    def register_new_user(self, email, password):
        reg_form_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        reg_form_email.send_keys(email)
        reg_form_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        reg_form_pass.send_keys(password)
        reg_form_pass_two = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_TWO_FIELD)
        reg_form_pass_two.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
