from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from sprint_5.utils.email_generator import EmailGenerator

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
# Переход на экран ввода кредов
driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]").click()
driver.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()

# ввод кредов с коротким паролем
driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys('Димооон')
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(
    EmailGenerator.generate_unique_email('gmail.com'))
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys('123')

# показ хинта о длинне пароля
driver.find_element(By.XPATH, ".//form//button").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                  ".//div[@class='input__container']//p")))
driver.quit()
