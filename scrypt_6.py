from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome(service=ChromeService(executable_path='C:/chromedriver/chromedriver'))
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    sleep(2)
    atrib = browser.find_element(By.ID, "treasure")
    x = calc((atrib.get_attribute("valuex")))
    input_answer = browser.find_element(By.ID, "answer")
    robot_chek = browser.find_element(By.ID,"robotCheckbox")
    robots_rule =  browser.find_element(By.ID, "robotsRule")
    input_answer.send_keys(x)
    robots_rule.click()
    robot_chek.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    sleep(10)
    browser.quit()
