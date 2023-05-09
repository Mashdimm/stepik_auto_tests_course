from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value_sum = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(value_sum))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    sleep(10)
finally:
    browser.quit()
