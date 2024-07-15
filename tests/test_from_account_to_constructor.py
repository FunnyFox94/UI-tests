from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


def test_from_account_to_constructor(driver):
    # авторизация
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    driver.find_element(*locators.EMAIL_FIELD_ON_AUTH_FORM).send_keys('momo@yandex.ru')
    driver.find_element(*locators.PASSWORD_FIELD_ONAUTH_FORM).send_keys('124367')
    driver.find_element(*locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.ORDER_BUTTON))

    # переход в конструктор
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.SAVE_BUTTON_IN_ACCOUNT))
    driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()

    # проверка отображаение элементов главного экрана
    url = 'https://stellarburgers.nomoreparties.site/'
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.ORDER_BUTTON))
    assert driver.find_element(*locators.ORDER_BUTTON).text == 'Оформить заказ' and driver.current_url == url
