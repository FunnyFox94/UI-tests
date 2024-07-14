from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from sprint_5.utils.email_generator import EmailGenerator
from sprint_5.utils.password_generator import PasswordGenerator

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# путь до ввода кредов
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
driver.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()

# ввод кредов
driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input").send_keys('Димооон')
driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input").send_keys(
    EmailGenerator.generate_unique_email('gmail.com'))
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(PasswordGenerator.generate_unique_password())
driver.find_element(By.XPATH, ".//form//button").click()

# проверка, что после авторизации произошел редирект на /login
WebDriverWait(driver, 3).until(expected_conditions.url_matches('https://stellarburgers.nomoreparties.site/login'))

driver.quit()


