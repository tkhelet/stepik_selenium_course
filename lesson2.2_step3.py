import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element(By.CSS_SELECTOR, "[id=num1]")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "[id=num2]")
    y = y_element.text
    z = (int(x) + int(y))

    print(z)

      # Отправляем заполненную форму
    button1 = browser.find_element(By.CSS_SELECTOR, "[id=dropdown]")
    button1.click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    button3 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()