from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Dmitrii")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Vlasov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("chertovskihorosh@rambler.ru")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']").send_keys("+12345678910")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys("Worldwide")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
