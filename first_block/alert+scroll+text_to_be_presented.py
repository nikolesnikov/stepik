from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    but.click()
    x = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x = x.text
    y = calc(x)
    answ = browser.find_element(By.ID, "answer")
    answ.send_keys(y)
    sub = browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    time.sleep(10)
    browser.quit()
