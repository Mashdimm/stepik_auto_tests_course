from selenium import webdriver
from selenium.webdriver.common.by import By
import random
letters = "abcdefghijklmnopqrstuvwxyz"
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")


elements = browser.find_elements(By.CSS_SELECTOR, "input")
for element in elements:
    element.send_keys("".join(random.choice(letters) for _ in range(5)))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)

browser.quit()

