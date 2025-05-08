from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


      # Отправляем заполненную форму
    button1 = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
    button1.send_keys("Имя")

    button2 = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
    button2.send_keys("Фамилия")

    button3 = browser.find_element(By.CSS_SELECTOR, "[name=email]")
    button3.send_keys("stepik@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    button5 = browser.find_element(By.CSS_SELECTOR, "[id=file]")
    button5.send_keys(file_path)

    button4 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()