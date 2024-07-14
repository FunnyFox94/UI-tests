from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# авторизация
driver.find_element(By.XPATH, ".//section//div//button[contains(text(), 'Войти в аккаунт')]").click()
driver.find_element(By.XPATH, ".//input[@type='text']").send_keys('momo@yandex.ru')
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('124367')
driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()

# проверка отображаение элемента в авторизованной зоне
WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))
assert (driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").text == 'Оформить заказ'
        and driver.current_url == 'https://stellarburgers.nomoreparties.site/')

driver.quit()
