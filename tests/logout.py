from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# авторизация
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
driver.find_element(By.XPATH, ".//input[@type='text']").send_keys('momo@yandex.ru')
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('124367')
driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()

WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))

# переход в личный кабинет
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
WebDriverWait(driver, 5).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Сохранить')]")))

# совершение логаута
driver.find_element(By.XPATH, ".//button[contains(text(), 'Выход')]").click()
WebDriverWait(driver, 5).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Войти')]")))
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()
