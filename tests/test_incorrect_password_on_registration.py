from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.email_generator import EmailGenerator as EG
import locators


def test_incorrect_password_on_registration(driver):
    # Переход на экран ввода кредов
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    driver.find_element(*locators.REGISTER_ACCOUNT_LINK).click()

    # ввод кредов с коротким паролем
    driver.find_element(*locators.NAME_FIELD_ON_REGISTRATION_FORM).send_keys('Димооон')
    driver.find_element(*locators.EMAIL_FIELD_ON_REGISTRATION_FORM).send_keys(EG.generate_unique_email('gmail.com'))
    driver.find_element(*locators.PASSWORD_FIELD_ON_REGISTRATION_FORM).send_keys('123')

    # показ хинта о длинне пароля
    driver.find_element(*locators.REGISTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.HINT_BAD_PASSWORD))
