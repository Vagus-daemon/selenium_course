from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def registration1():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    browser.find_element(By.XPATH, "//input[@type='text']").send_keys("Dmitrii")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Markov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("horosh@rambler.ru")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']").send_keys("+12345678910")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys("Worldwide")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    browser.quit()


if __name__ == '__main__':
    print(registration1())
