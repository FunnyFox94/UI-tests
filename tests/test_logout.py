from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import constants
import locators


def test_logout(driver):
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    driver.find_element(*locators.EMAIL_FIELD_ON_AUTH_FORM).send_keys('momo@yandex.ru')
    driver.find_element(*locators.PASSWORD_FIELD_ONAUTH_FORM).send_keys('124367')
    driver.find_element(*locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.ORDER_BUTTON))

    # переход в личный кабинет
    driver.find_element(*locators.ACCOUNT_BUTTON_IN_HEADER).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.SAVE_BUTTON_IN_ACCOUNT))

    # совершение логаута
    driver.find_element(*locators.EXIT_BUTTON_IN_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON))
    assert driver.current_url == constants.LOGIN_URL
