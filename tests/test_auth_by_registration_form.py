from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import constants
import locators


def test_auth_by_registration_form(driver):
    # авторизация
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    driver.find_element(*locators.REGISTER_ACCOUNT_LINK).click()
    driver.find_element(*locators.LOGIN_LINK).click()
    driver.find_element(*locators.EMAIL_FIELD_ON_AUTH_FORM).send_keys('momo@yandex.ru')
    driver.find_element(*locators.PASSWORD_FIELD_ONAUTH_FORM).send_keys('124367')
    driver.find_element(*locators.LOGIN_BUTTON).click()

    # проверка отображаение элемента в авторизованной зоне
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.ORDER_BUTTON))
    assert driver.find_element(*locators.ORDER_BUTTON).text == 'Оформить заказ' and driver.current_url == constants.BASE_URL
