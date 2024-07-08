import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button2 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y_element = browser.find_element(By.ID, "answer")
    y = calc(x)
    y_element.send_keys(y)

    # ждем загрузки страницы
    time.sleep(1)

# Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()