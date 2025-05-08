from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


      # Отправляем заполненную форму
    button4 = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']").click()

    button1 = browser.switch_to.alert
    button1.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    print(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
    button2.send_keys(y)

    button3 = browser.find_element(By.XPATH, "//button[text()='Submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()