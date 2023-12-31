from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs '
                                            '[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_TWO_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    WRITE_REVIEW = (By.CSS_SELECTOR, '#write_review')
    PRICE_PRODUCT_MAIN = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in '
                                         '> .alertinner strong')
    NAME_PRODUCT_MAIN = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    NAME_MESSAGE_PRODUCT = (By.CSS_SELECTOR, '#messages > '
                                             '.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) '
                                             '.alertinner strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > .alertinner')


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '#basket_formset')
