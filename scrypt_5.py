from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    x = calc(browser.find_element(By.ID, "input_value").text)
    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(x)

    for_robot = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    for_robot.click()

    robot_rules = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_rules.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    sleep(15)




finally:
    browser.quit()

