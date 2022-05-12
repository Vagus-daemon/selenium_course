from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
)
browser.find_element(By.ID, "book").click()

time.sleep(10)

browser.quit()
