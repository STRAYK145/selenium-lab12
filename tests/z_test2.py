from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.binary_location = r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chrome-win64\chrome.exe"
service = Service(r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chromedriver.exe")

browser = webdriver.Chrome(service=service, options=options)
browser.get('https://store.steampowered.com')

time.sleep(2)

# Находим поле поиска и вводим запрос
search = browser.find_element(by=By.CSS_SELECTOR, value='input._2tlUAG6WNyYFlk9caIiLj5[type="text"]')
search.send_keys('Counter-Strike 2')
search.send_keys(Keys.ENTER)

time.sleep(3)

try:
    # Проверяем что в результатах есть нужная игра
    assert 'Counter-Strike 2' in browser.page_source
    print('Тест 2 пройден успешно: игра найдена в результатах поиска')
except Exception as err:
    print('Тест 2 не пройден:', err)

browser.close()