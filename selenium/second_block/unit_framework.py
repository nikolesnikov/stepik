from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()


def test_0(link):
    browser.get(link)

    input1 = browser.find_element(
        By.XPATH, "//input[@placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.XPATH, "//input[@placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("jose@yandex.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    return welcome_text


class Test1(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        rez1 = test_0(link)
        self.assertEqual(rez1, "Congratulations! You have successfully registered!")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        rez2 = test_0(link)
        self.assertEqual(rez2, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
