from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text

    y = calc(x)

    answ = browser.find_element(By.ID, "answer")
    answ.send_keys(y)

    but = browser.find_element(By.CSS_SELECTOR, "button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()
