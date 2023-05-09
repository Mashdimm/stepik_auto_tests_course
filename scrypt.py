from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)  # неявное ожидание, чтобы убедиться, что страница полностью загружена

    browser.get(link)

    first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")

    # формируем случайные строки для заполнения полей
    letters = string.ascii_lowercase
    first_name_value = "".join(random.choice(letters) for _ in range(7))
    last_name_value = "".join(random.choice(letters) for _ in range(10))
    email_value = "".join(random.choice(letters) for _ in range(7)) + "@example.com"

    first_name.send_keys(first_name_value)
    last_name.send_keys(last_name_value)
    email.send_keys(email_value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # проверяем, что сообщение об успешной регистрации появилось на странице
    success_message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Congratulations! You have successfully registered!" in success_message.text

finally:
    browser.quit()

