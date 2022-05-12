from selenium import webdriver
import time

from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    z = int(browser.find_element(By.XPATH, "//span[@id='num1']")) + int(browser.find_element(By.XPATH, "//span[@id='num2']"))
    browser.find_element(By.XPATH, "//select[@id='dropdown']").click()
    browser.find_element(By.XPATH, "//option[contains(string(), 'z')]").click()
    browser.find_element(By.XPATH, "//button[contains(string(), 'Submit')]").click()


