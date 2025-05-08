from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим WebDriver проверять цену в течение 5 секунд, пока она не снизится до $100
    button1 = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))


    button4 = browser.find_element(By.XPATH, "//button[text()='Book']").click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


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

