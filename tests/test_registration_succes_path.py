from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from utils.email_generator import EmailGenerator as EG
from utils.password_generator import PasswordGenerator as PG

import locators


def test_registration_succes_path(driver):
    # путь до ввода кредов
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    driver.find_element(*locators.REGISTER_ACCOUNT_LINK).click()

    # ввод кредов
    driver.find_element(*locators.NAME_FIELD_ON_REGISTRATION_FORM).send_keys('Димооон')
    driver.find_element(*locators.EMAIL_FIELD_ON_REGISTRATION_FORM).send_keys(EG.generate_unique_email('gmail.com'))
    driver.find_element(*locators.PASSWORD_FIELD_ON_REGISTRATION_FORM).send_keys(PG.generate_unique_password())
    driver.find_element(*locators.REGISTER_ACCOUNT_BUTTON).click()

    # проверка, что после авторизации произошел редирект на /login
    WebDriverWait(driver, 3).until(expected_conditions.url_matches(constants.LOGIN_URL))
