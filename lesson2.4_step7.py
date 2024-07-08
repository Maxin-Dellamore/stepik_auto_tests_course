from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "button")
button.click()
