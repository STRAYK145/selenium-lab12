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
browser.get('https://steamcommunity.com/market')

time.sleep(2)

# Находим поле поиска на торговой площадке
search = browser.find_element(by=By.CSS_SELECTOR, value='input[type="text"]')
search.send_keys('AK-47')
search.send_keys(Keys.ENTER)

time.sleep(3)

try:
    # Проверяем что в результатах есть предметы с AK-47
    assert 'AK-47' in browser.page_source
    print('Тест 3 пройден успешно: предметы AK-47 найдены на торговой площадке')
except Exception as err:
    print('Тест 3 не пройден:', err)

browser.close()