from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# задаем переменные для секций
filling = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Начинки')]")
sauce = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Соусы')]")
bread = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Булки')]")

# скролл к начинкам
driver.execute_script("arguments[0].scrollIntoView();", filling)
WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Начинки')]")))
# скрол к соусам
driver.execute_script("arguments[0].scrollIntoView();", sauce)
WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Соусы')]")))
# скрол к соусам
driver.execute_script("arguments[0].scrollIntoView();", bread)
WebDriverWait(driver, 3).until(expected_conditions.
                               visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Булки')]")))

