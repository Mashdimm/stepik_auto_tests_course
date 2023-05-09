from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import math

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

try:
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, link_text))
    )
    link_element.click()

    input1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "first_name"))
    )
    input1.send_keys("Ivan")

    input2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "last_name"))
    )
    input2.send_keys("Petrov")

    input3 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control.city"))
    )
    input3.send_keys("Smolensk")

    input4 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    input4.send_keys("Russia")

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
    )
    button.click()
    time.sleep(30)

finally:
    browser.quit()

