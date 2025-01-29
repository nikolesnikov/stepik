from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    num1 = int(num1)
    num2 = int(num2)
    sm = num1 + num2
    sm = str(sm)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sm)

    but = browser.find_element(By.CSS_SELECTOR, "button.btn")
    but.click()

finally:
    time.sleep(10)
    browser.quit()
