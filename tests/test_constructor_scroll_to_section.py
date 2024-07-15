from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


def test_constructor_scroll_to_section(driver):
    # задаем переменные для секций
    filling = driver.find_element(*locators.FILLINGS_SECTIONS)
    sauce = driver.find_element(*locators.SAUCES_SECTION)
    bread = driver.find_element(*locators.BREAD_SECTION)

    # скролл к начинкам
    driver.execute_script("arguments[0].scrollIntoView();", filling)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.FILLINGS_SECTIONS))
    # скрол к соусам
    driver.execute_script("arguments[0].scrollIntoView();", sauce)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.SAUCES_SECTION))
    # скрол к соусам
    driver.execute_script("arguments[0].scrollIntoView();", bread)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.BREAD_SECTION))
