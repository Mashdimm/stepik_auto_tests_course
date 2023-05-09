from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = calc(browser.find_element(By.ID, "input_value").text)

    input_x_value = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_x_value)
    input_x_value.send_keys(x_value)

    robot_chek = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_chek)
    robot_chek.click()

    robot_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    sleep(10)

except Exception as e:
    print(e)
finally:
    browser.quit()
