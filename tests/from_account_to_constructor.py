from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# авторизация
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
driver.find_element(By.XPATH, ".//input[@type='text']").send_keys('momo@yandex.ru')
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('124367')
driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))

# переход в конструктор
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
WebDriverWait(driver, 5).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Сохранить')]")))
driver.find_element(By.XPATH, ".//p[contains(text(), 'Конструктор')]").click()


# проверка отображаение элементов главного экрана
WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))
assert (driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").text == 'Оформить заказ'
        and driver.current_url == 'https://stellarburgers.nomoreparties.site/')

driver.quit()